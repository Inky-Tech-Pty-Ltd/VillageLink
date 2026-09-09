from __future__ import annotations

import sys
from dataclasses import dataclass
from urllib.parse import urlparse

from PySide6.QtCore import QTimer, QUrl
from PySide6.QtGui import QGuiApplication
from PySide6.QtWebEngineCore import QWebEnginePage
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWidgets import (
    QApplication,
    QHBoxLayout,
    QLineEdit,
    QMainWindow,
    QPushButton,
    QSplitter,
    QVBoxLayout,
    QWidget,
)

from .codec import parse as parse_village_link


HOME_HTML = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Village Link</title>
<style>
  :root { color-scheme: light; }
  * { box-sizing: border-box; }
  body {
    margin: 0;
    min-height: 100vh;
    display: grid;
    place-items: center;
    background: #ffffff;
    color: #202124;
    font-family: Arial, Helvetica, sans-serif;
  }
  main {
    width: min(760px, calc(100vw - 64px));
    text-align: center;
    transform: translateY(-6vh);
  }
  .mark {
    font-size: 64px;
    line-height: 1;
    margin-bottom: 10px;
    color: #d81b86;
  }
  h1 {
    margin: 0 0 34px;
    font-size: 48px;
    font-weight: 400;
    letter-spacing: -1px;
  }
  .trust {
    width: 100%;
    height: 54px;
    border: 1px solid #dfe1e5;
    border-radius: 27px;
    box-shadow: 0 1px 6px rgba(32, 33, 36, .18);
    display: flex;
    align-items: center;
    padding: 0 20px;
    color: #9aa0a6;
    font-size: 17px;
    text-align: left;
  }
  .trust::before {
    content: "⌕";
    margin-right: 14px;
    font-size: 25px;
    color: #5f6368;
  }
  .bookmarks {
    display: flex;
    justify-content: center;
    gap: 12px;
    margin-top: 24px;
    flex-wrap: wrap;
  }
  .bookmark {
    display: inline-block;
    padding: 10px 15px;
    border: 1px solid #dadce0;
    border-radius: 18px;
    color: #3c4043;
    text-decoration: none;
    background: #f8f9fa;
    font-size: 14px;
  }
  .bookmark:hover {
    background: #f1f3f4;
  }
</style>
</head>
<body>
  <main>
    <div class="mark">✱</div>
    <h1>Village Link</h1>
    <div class="trust">Trust engine</div>
    <div class="bookmarks">
      <a class="bookmark" href="https://village.link/wiki/index.php/Asha_Bhosle">Asha Bhosle</a>
      <a class="bookmark" href="https://village.link/wiki/index.php/Puck-GPT">Puck-GPT</a>
    </div>
  </main>
</body>
</html>
"""


def village_targets(raw_url: str) -> tuple[str, str] | None:
    """Return A and B when *raw_url* is a serialized Village Link."""
    try:
        return parse_village_link(raw_url)
    except ValueError:
        return None


@dataclass(frozen=True)
class BrowserState:
    """A structural browser state worth restoring with the shell Back button."""

    left: str
    right: str | None = None


class VillagePage(QWebEnginePage):
    """Web page that hands main-frame navigation back to the browser shell."""

    def __init__(self, browser: "Browser", parent: QWebEngineView, side: str) -> None:
        super().__init__(parent)
        self.browser = browser
        self.side = side

    def acceptNavigationRequest(self, url: QUrl, nav_type, is_main_frame: bool) -> bool:  # noqa: N802
        if is_main_frame:
            targets = village_targets(url.toString())
            if targets:
                left, right = targets
                QTimer.singleShot(0, lambda: self.browser.open_village_link(left, right, remember=True))
                return False

            if self.side == "left" and self.browser.consume_internal_left_navigation(url):
                return super().acceptNavigationRequest(url, nav_type, is_main_frame)

            # Leaving a comparison through an ordinary link on the left is a
            # structural transition: remember the split so Back can reconstruct it.
            if self.side == "left" and self.browser.is_split():
                raw_url = url.toString()
                QTimer.singleShot(0, lambda: self.browser.open_single(raw_url, remember=True))
                return False

        return super().acceptNavigationRequest(url, nav_type, is_main_frame)


class Browser(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Village Link Browser — prototype")
        self.resize(1400, 900)
        self._internal_left_url: str | None = None
        self._state_history: list[BrowserState] = []

        self.back = QPushButton("← Back")
        self.back.setToolTip("Go back, restoring a Village Link split when necessary")
        self.back.clicked.connect(self.go_back)

        self.address = QLineEdit()
        self.address.setPlaceholderText("Enter a URL or Village Link")
        self.address.returnPressed.connect(self.navigate)

        go = QPushButton("Go")
        go.clicked.connect(self.navigate)

        self.promote = QPushButton("Promote right")
        self.promote.setToolTip("Make the right-hand page the ordinary full-width browsing context")
        self.promote.clicked.connect(self.promote_right)
        self.promote.hide()

        toolbar = QHBoxLayout()
        toolbar.addWidget(self.back)
        toolbar.addWidget(self.address)
        toolbar.addWidget(go)
        toolbar.addWidget(self.promote)

        self.left = QWebEngineView()
        self.right = QWebEngineView()
        self.left.setPage(VillagePage(self, self.left, "left"))
        self.right.setPage(VillagePage(self, self.right, "right"))

        self.left.urlChanged.connect(self._left_url_changed)

        self.splitter = QSplitter()
        self.splitter.addWidget(self.left)
        self.splitter.addWidget(self.right)

        layout = QVBoxLayout()
        layout.addLayout(toolbar)
        layout.addWidget(self.splitter)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        self.show_home()

    def is_split(self) -> bool:
        return not self.right.isHidden()

    def current_state(self) -> BrowserState:
        right = self.right.url().toString() if self.is_split() else None
        return BrowserState(self.left.url().toString(), right)

    def remember_state(self) -> None:
        state = self.current_state()
        if not state.left:
            return
        if not self._state_history or self._state_history[-1] != state:
            self._state_history.append(state)

    def consume_internal_left_navigation(self, url: QUrl) -> bool:
        """Return True once for the left URL intentionally loaded by the browser shell."""
        if self._internal_left_url is None:
            return False
        if url.toString() != self._internal_left_url:
            return False
        self._internal_left_url = None
        return True

    def _left_url_changed(self, url: QUrl) -> None:
        if not self.is_split():
            self.address.setText(url.toString())

    def show_home(self) -> None:
        """Show the deliberately minimal demo landing page."""
        self._internal_left_url = None
        self.right.hide()
        self.promote.hide()
        self.address.clear()
        self.left.setHtml(HOME_HTML, QUrl("https://home.village.link/"))

    def open_single(self, url: str, *, remember: bool = False) -> None:
        """Browse one URL at full width, optionally remembering the state being left."""
        if remember:
            self.remember_state()
        self._internal_left_url = None
        self.right.hide()
        self.promote.hide()
        self.address.setText(url)
        self.left.setUrl(QUrl(url))

    def open_village_link(self, left: str, right: str, *, remember: bool = False) -> None:
        """Display Village Link endpoints A and B side by side."""
        if remember:
            self.remember_state()
        self._internal_left_url = QUrl(left).toString()
        self.left.setUrl(QUrl(left))
        self.right.setUrl(QUrl(right))
        self.right.show()
        self.promote.show()
        self.splitter.setSizes([1, 1])

    def restore_state(self, state: BrowserState) -> None:
        """Restore a saved single or split structural state without adding history."""
        if state.right is None:
            self.open_single(state.left)
        else:
            self.open_village_link(state.left, state.right)

    def go_back(self) -> None:
        """Go back one human-visible step, including across split/single transitions."""
        saved = self._state_history[-1] if self._state_history else None

        if self.is_split():
            # While exploring the right-hand memory system, ordinary web history
            # is the nearest thing behind us. Only restore an earlier structural
            # state once that local history is exhausted.
            if self.right.history().canGoBack():
                self.right.back()
                return
            if saved is not None:
                self.restore_state(self._state_history.pop())
            return

        # In single-pane mode, a saved split may be the boundary immediately
        # behind the current ordinary browsing run. Preserve ordinary one-page-at-
        # a-time history until the next Back would cross that boundary.
        if saved is not None and saved.right is not None:
            current = self.left.url().toString()

            # Promote-right copies B into the left pane. In that case the split is
            # immediately behind the promoted page, regardless of older left-pane
            # web history retained by Qt.
            if current == saved.right:
                self.restore_state(self._state_history.pop())
                return

            history = self.left.history()
            if history.canGoBack():
                previous = history.backItem().url().toString()
                if previous == saved.left:
                    self.restore_state(self._state_history.pop())
                    return
                self.left.back()
                return

            self.restore_state(self._state_history.pop())
            return

        # No split boundary is pending: behave like a conventional browser.
        if self.left.history().canGoBack():
            self.left.back()
            return

        if saved is not None:
            self.restore_state(self._state_history.pop())

    def promote_right(self) -> None:
        """Make the current right-hand page the new ordinary browsing context."""
        if self.is_split():
            self.remember_state()
            self.open_single(self.right.url().toString())

    def navigate(self) -> None:
        raw = self.address.text().strip()
        if not raw:
            self.show_home()
            return

        if not urlparse(raw).scheme:
            raw = "https://" + raw
            self.address.setText(raw)

        targets = village_targets(raw)
        if targets:
            self.open_village_link(*targets, remember=bool(self.left.url().toString()))
        else:
            self.open_single(raw)

    def place_on_screen(self) -> None:
        """Fit and centre the prototype inside the primary screen's usable area."""
        screen = QGuiApplication.primaryScreen()
        if screen is None:
            return

        available = screen.availableGeometry()
        width = min(self.width(), available.width())
        height = min(self.height(), available.height())
        self.resize(width, height)
        self.move(
            available.x() + (available.width() - width) // 2,
            available.y() + (available.height() - height) // 2,
        )


def main() -> None:
    app = QApplication(sys.argv)
    browser = Browser()
    browser.place_on_screen()
    browser.show()
    raise SystemExit(app.exec())


if __name__ == "__main__":
    main()

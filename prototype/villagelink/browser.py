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

        self.address = QLineEdit("https://village.link/wiki/index.php/Asha_Bhosle")
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

        self.navigate()

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
        """Undo shell transitions first; otherwise use the active page's web history."""
        if self._state_history:
            self.restore_state(self._state_history.pop())
            return

        # Once structural history is exhausted, behave like a conventional Back
        # button. In split mode the right pane is the active exploratory context;
        # in single mode the left pane is the browser.
        active = self.right if self.is_split() else self.left
        if active.history().canGoBack():
            active.back()

    def promote_right(self) -> None:
        """Make the current right-hand page the new ordinary browsing context."""
        if self.is_split():
            self.remember_state()
            self.open_single(self.right.url().toString())

    def navigate(self) -> None:
        raw = self.address.text().strip()
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

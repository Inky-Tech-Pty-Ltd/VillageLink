from __future__ import annotations

import sys
from urllib.parse import urlparse

from PySide6.QtCore import QTimer, QUrl
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


class VillagePage(QWebEnginePage):
    """Web page that hands Village Link clicks back to the browser shell."""

    def __init__(self, browser: "Browser", parent: QWebEngineView) -> None:
        super().__init__(parent)
        self.browser = browser

    def acceptNavigationRequest(self, url: QUrl, nav_type, is_main_frame: bool) -> bool:  # noqa: N802
        if is_main_frame:
            targets = village_targets(url.toString())
            if targets:
                # Do not change either QWebEngineView synchronously from inside
                # Qt's navigation-acceptance callback. On Windows/QtWebEngine this
                # can terminate the process in native code before Python gets a
                # chance to print a traceback. Hand the work back to the event
                # loop instead.
                left, right = targets
                QTimer.singleShot(0, lambda: self.browser.open_village_link(left, right))
                return False
        return super().acceptNavigationRequest(url, nav_type, is_main_frame)


class Browser(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Village Link Browser — prototype")
        self.resize(1400, 900)

        self.address = QLineEdit("https://village.link/wiki/index.php/Asha_Bhosle")
        self.address.returnPressed.connect(self.navigate)

        go = QPushButton("Go")
        go.clicked.connect(self.navigate)

        toolbar = QHBoxLayout()
        toolbar.addWidget(self.address)
        toolbar.addWidget(go)

        self.left = QWebEngineView()
        self.right = QWebEngineView()
        self.left.setPage(VillagePage(self, self.left))
        self.right.setPage(VillagePage(self, self.right))

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

    def _left_url_changed(self, url: QUrl) -> None:
        """Keep the address bar useful during ordinary single-pane browsing."""
        if self.right.isHidden():
            self.address.setText(url.toString())

    def open_village_link(self, left: str, right: str) -> None:
        """Display Village Link endpoints A and B side by side."""
        self.left.setUrl(QUrl(left))
        self.right.setUrl(QUrl(right))
        self.right.show()
        self.splitter.setSizes([1, 1])

    def navigate(self) -> None:
        raw = self.address.text().strip()
        if not urlparse(raw).scheme:
            raw = "https://" + raw
            self.address.setText(raw)

        targets = village_targets(raw)
        if targets:
            self.open_village_link(*targets)
        else:
            self.right.hide()
            self.left.setUrl(QUrl(raw))


def main() -> None:
    app = QApplication(sys.argv)
    browser = Browser()
    browser.show()
    raise SystemExit(app.exec())


if __name__ == "__main__":
    main()

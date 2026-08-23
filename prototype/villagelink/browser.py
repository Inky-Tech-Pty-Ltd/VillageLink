from __future__ import annotations

import sys
from urllib.parse import parse_qs, urlparse

from PySide6.QtCore import QUrl
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
from PySide6.QtWebEngineWidgets import QWebEngineView


def village_targets(raw_url: str) -> tuple[str, str] | None:
    parsed = urlparse(raw_url)
    if parsed.netloc.lower() != "village.link":
        return None
    if parsed.path.rstrip("/") != "/demo":
        return None

    query = parse_qs(parsed.query)
    left = query.get("left", [None])[0]
    right = query.get("right", [None])[0]
    if not left or not right:
        return None
    return left, right


class Browser(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Village Link Browser — prototype")
        self.resize(1400, 900)

        self.address = QLineEdit("https://example.com")
        self.address.returnPressed.connect(self.navigate)

        go = QPushButton("Go")
        go.clicked.connect(self.navigate)

        toolbar = QHBoxLayout()
        toolbar.addWidget(self.address)
        toolbar.addWidget(go)

        self.left = QWebEngineView()
        self.right = QWebEngineView()

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

    def navigate(self) -> None:
        raw = self.address.text().strip()
        if not urlparse(raw).scheme:
            raw = "https://" + raw
            self.address.setText(raw)

        targets = village_targets(raw)
        if targets:
            left, right = targets
            self.left.setUrl(QUrl(left))
            self.right.setUrl(QUrl(right))
            self.right.show()
            self.splitter.setSizes([1, 1])
        else:
            self.left.setUrl(QUrl(raw))
            self.right.hide()


def main() -> None:
    app = QApplication(sys.argv)
    browser = Browser()
    browser.show()
    raise SystemExit(app.exec())


if __name__ == "__main__":
    main()

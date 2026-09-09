from __future__ import annotations

import sys

from PySide6.QtGui import QGuiApplication
from PySide6.QtWidgets import (
    QApplication,
    QFormLayout,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget,
)

from .codec import make


class Composer(QMainWindow):
    """Tiny stateless Village Link composer for demos and testing."""

    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Village Link Composer — prototype")
        self.resize(820, 260)

        self.endpoint_a = QLineEdit()
        self.endpoint_a.setPlaceholderText("https://…")

        self.endpoint_b = QLineEdit()
        self.endpoint_b.setPlaceholderText("https://…")

        self.output = QLineEdit()
        self.output.setReadOnly(True)
        self.output.setPlaceholderText("Village Link appears here")

        compose = QPushButton("Compose")
        compose.clicked.connect(self.compose)

        copy = QPushButton("Copy")
        copy.clicked.connect(self.copy_output)

        form = QFormLayout()
        form.addRow("A", self.endpoint_a)
        form.addRow("B", self.endpoint_b)
        form.addRow("Village Link", self.output)

        actions = QHBoxLayout()
        actions.addStretch()
        actions.addWidget(compose)
        actions.addWidget(copy)

        layout = QVBoxLayout()
        layout.addWidget(QLabel("Compose one Village Link from two endpoint URLs."))
        layout.addLayout(form)
        layout.addLayout(actions)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        self.endpoint_a.returnPressed.connect(self.compose)
        self.endpoint_b.returnPressed.connect(self.compose)

    def compose(self) -> None:
        a = self.endpoint_a.text().strip()
        b = self.endpoint_b.text().strip()

        if not a or not b:
            self.output.clear()
            self.statusBar().showMessage("Enter both endpoint URLs.")
            return

        self.output.setText(make(a, b))
        self.statusBar().showMessage("Village Link composed.")

    def copy_output(self) -> None:
        value = self.output.text()
        if not value:
            self.statusBar().showMessage("Compose a Village Link first.")
            return

        QGuiApplication.clipboard().setText(value)
        self.statusBar().showMessage("Copied to clipboard.")


def main() -> None:
    app = QApplication(sys.argv)
    composer = Composer()
    composer.show()
    raise SystemExit(app.exec())


if __name__ == "__main__":
    main()

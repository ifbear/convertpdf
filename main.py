import sys
from PyQt6.QtWidgets import QApplication, QScrollArea
from Home import Home


def init():
    app = QApplication(sys.argv)

    home = Home()

    sys.exit(app.exec())

if __name__ == '__main__':
    init()


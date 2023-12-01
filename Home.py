import sys
from PyQt6.QtWidgets import QWidget

class Home(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.resize(1000, 600)
        self.move(100, 100)
        self.setWindowTitle("Convert PDF")
        self.show()

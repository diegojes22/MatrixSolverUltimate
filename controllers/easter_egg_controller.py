from PyQt5.QtWidgets import QDialog
from ui.easter_egg import Ui_Dialog

class EasterEggController(QDialog, Ui_Dialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("Nico y la China")

    def show(self):
        super().show()

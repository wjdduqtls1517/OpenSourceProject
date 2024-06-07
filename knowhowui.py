import sys
import os
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QTextEdit, QDialog, QMessageBox, QDesktopWidget, QComboBox, QInputDialog)
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
class InputDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('노하우 작성')
        self.text_edit = QTextEdit()
        #크기 조절
        self.setFixedSize(1000, 800)

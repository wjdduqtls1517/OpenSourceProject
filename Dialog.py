<<<<<<< HEAD

=======
>>>>>>> origin/feature_knowhowreal
import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QLineEdit, QPushButton,
                             QVBoxLayout, QHBoxLayout, QDesktopWidget, QTextEdit, QDialog)
from PyQt5.QtGui import QFont, QScreen
from PyQt5.QtCore import Qt

class InputDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('텍스트 입력')
        self.text_edit = QTextEdit()
        layout = QVBoxLayout()
        layout.addWidget(self.text_edit)
        confirm_button = QPushButton('확인')
        confirm_button.clicked.connect(self.accept)
        layout.addWidget(confirm_button)
        self.setLayout(layout)
<<<<<<< HEAD
 if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = QuestionWindow()
    sys.exit(app.exec_())
=======
>>>>>>> origin/feature_knowhowreal

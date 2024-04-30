import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QDesktopWidget
from PyQt5.QtGui import QFont


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('My First Application')
        self.resize(700, 500)

        # 창을 화면의 정가운데에 위치시키기
        self.center()

        def center(self):
            # 화면의 가운데 위치 구하기
            qr = self.frameGeometry()
            cp = QDesktopWidget().availableGeometry().center()
            qr.moveCenter(cp)
            self.move(qr.topLeft())
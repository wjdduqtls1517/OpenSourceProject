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

        # 모든 위젯에 대해 Arial 폰트 설정
        font = QFont('Arial', 12)

        # '건강관리' QLabel 추가
        lbl = QLabel('건강관리', self)
        lbl.setFont(font)  # 폰트 설정
        lbl.adjustSize()  # 텍스트에 맞게 크기 조정
        lbl.move(int(self.width() / 2 - lbl.width() / 2), 20)  # 창 상단 중앙에 배치





    def center(self):
        # 화면의 가운데 위치 구하기
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())




if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())

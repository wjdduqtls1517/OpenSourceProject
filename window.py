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

            # 'Exit' 버튼 추가
            self.add_exit_button(font)

            self.show()

            def add_exit_button(self, font):
                btn_width, btn_height = 70, 30  # 버튼의 폭과 높이
                btn_x = self.width() - btn_width - 10  # 창의 너비에서 버튼의 폭과 간격을 뺀 값
                btn_y = self.height() - btn_height - 10  # 창의 높이에서 버튼의 높이와 간격을 뺀 값
                btn = QPushButton('나가기', self)
                btn.setGeometry(btn_x, btn_y, btn_width, btn_height)  # 위치와 크기 설정
                btn.setFont(font)  # 폰트 설정
                btn.clicked.connect(self.exit_application)  # 버튼 클릭 시 종료 함수 연결

            def exit_application(self):
                QApplication.instance().quit()

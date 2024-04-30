from PyQt5.QtWidgets import QApplication, QPushButton


def add_exit_button(self):
    btn_width, btn_height = 70, 30  # 버튼의 폭과 높이
    btn_x = self.width() - btn_width - 10  # 창의 너비에서 버튼의 폭과 간격을 뺀 값
    btn_y = self.height() - btn_height - 10  # 창의 높이에서 버튼의 높이와 간격을 뺀 값
    btn = QPushButton('나가기', self)
    btn.setGeometry(btn_x, btn_y, btn_width, btn_height)  # 위치와 크기 설정
    btn.clicked.connect(self.exit_application)  # 버튼 클릭 시 종료 함수 연결


def exit_application(self):
    QApplication.instance().quit()

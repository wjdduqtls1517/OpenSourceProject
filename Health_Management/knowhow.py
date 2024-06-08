import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QLineEdit, QPushButton,
                             QVBoxLayout, QHBoxLayout, QDesktopWidget, QTextEdit, QDialog)
from PyQt5.QtGui import QFont, QScreen
from PyQt5.QtCore import Qt

class QuestionWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('질병 - 노하우')
        self.resize(800, 1200)  # 게시판의 크기를 조정
        self.center()

        # 폰트 설정
        font_title = QFont('Arial', 20)
        font_label = QFont('Arial', 18)
        font_button = QFont('Arial', 16)

        # 메인 레이아웃 설정
        main_layout = QVBoxLayout()

        # 제목 레이블
        title_label = QLabel('(질병) - 노하우', self)
        title_label.setFont(font_title)
        title_label.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(title_label)

        # 텍스트 게시판
        self.text_board = QTextEdit(self)
        self.text_board.setFont(font_label)
        self.text_board.setReadOnly(True)
        main_layout.addWidget(self.text_board)

        # 버튼 레이아웃
        button_layout = QHBoxLayout()

        # 이전 버튼
        prev_button = QPushButton('이전', self)
        prev_button.setFont(font_button)
        prev_button.clicked.connect(self.on_prev_click)
        button_layout.addWidget(prev_button)

        # 입력 버튼
        write_button = QPushButton('입력', self)
        write_button.setFont(font_button)
        write_button.clicked.connect(self.on_write_click)
        button_layout.addWidget(write_button)

        main_layout.addLayout(button_layout)

        self.setLayout(main_layout)
        self.show()

        # 게시판에 초기 텍스트 추가
        self.add_text_to_board("텍스트")

            def center(self):
        qr = self.frameGeometry()
        screen = QApplication.primaryScreen()
        cp = screen.availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def on_prev_click(self):
        print('이전')

    def on_write_click(self):
        input_dialog = InputDialog(self)
        if input_dialog.exec_():
            text = input_dialog.text_edit.toPlainText()
            self.add_text_to_board(text)

    def add_text_to_board(self, text):
        current_text = self.text_board.toPlainText()
        self.text_board.setPlainText(current_text + "\n" + text)


        if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = QuestionWindow()
    sys.exit(app.exec_())

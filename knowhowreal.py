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

        # 폰트 설정
        font_label = QFont('Arial', 18)
        font_button = QFont('Arial', 16)

        #노하우 작성 창
        layout = QVBoxLayout()
        layout.addWidget(QLabel('노하우:', self))
        layout.addWidget(self.text_edit)

        #노하우 작성 확인 버튼
        confirm_button = QPushButton('확인')
        confirm_button.setFont(font_button)
        confirm_button.clicked.connect(self.accept)
        layout.addWidget(confirm_button)

        # 설정한 폰트를 적용
        self.text_edit.setFont(font_label)
        confirm_button.setFont(font_button)
        self.setLayout(layout)

class QuestionWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('질병 - 노하우')
        self.resize(800, 1000)
        self.center()

        # 폰트 설정
        font_title = QFont('Arial', 24)
        font_label = QFont('Arial', 18)
        font_button = QFont('Arial', 16)

        main_layout = QVBoxLayout()

        # 제목 레이블
        self.title_label = QLabel('질병 노하우', self)
        self.title_label.setFont(font_title)
        self.title_label.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(self.title_label)

        # 질병 선택 콤보박스
        self.disease_combo = QComboBox(self)
        self.disease_combo.addItem("간질환")
        self.disease_combo.addItem("갑상선")
        self.disease_combo.addItem("고혈압")
        self.disease_combo.addItem("골다공증")
        self.disease_combo.addItem("관절염")
        self.disease_combo.addItem("노인성 빈혈")
        self.disease_combo.addItem("노인성 우울증")
        self.disease_combo.addItem("녹내장")
        self.disease_combo.addItem("뇌동맥류")
        self.disease_combo.addItem("노졸증")
        self.disease_combo.addItem("당뇨병")
        self.disease_combo.addItem("동맥경화증")
        self.disease_combo.addItem("변비")
        self.disease_combo.addItem("신장병")
        self.disease_combo.addItem("오십견")
        self.disease_combo.addItem("요통")
        self.disease_combo.addItem("위장병")
        self.disease_combo.addItem("치매")
        self.disease_combo.addItem("통풍")
        self.disease_combo.addItem("퇴행성 근골격장애")
        self.disease_combo.addItem("파킨슨병")
        self.disease_combo.currentTextChanged.connect(self.update_title_and_load_text)

        # 콤보박스 크기 조절
        self.disease_combo.setFixedSize(900, 80)

        # 콤보박스 폰트 설정
        combo_font = QFont('Arial', 16)
        self.disease_combo.setFont(combo_font)
        main_layout.addWidget(self.disease_combo)


        # 텍스트 게시판
        self.text_board = QTextEdit(self)
        self.text_board.setFont(font_label)
        self.text_board.setReadOnly(True)
        main_layout.addWidget(self.text_board)

        # 버튼 레이아웃
        button_layout = QHBoxLayout()

        # 이전 버튼
        prev_button = QPushButton('이전', self)
        prev_button.setFont(QFont('Noto Sans', 16))
        prev_button.setFixedSize(100, 40)
        prev_button.setStyleSheet("background-color: blue; color: white;")
        prev_button.clicked.connect(self.on_prev_click)  # 이전 버튼 클릭 시 처리할 슬롯 연결
        button_layout.addWidget(prev_button, alignment=Qt.AlignLeft)

        # 입력 버튼
        write_button = QPushButton('작성', self)
        write_button.setFont(QFont('Noto Sans', 16))
        write_button.setFixedSize(100, 40)
        write_button.setStyleSheet("background-color: blue; color: white;")
        write_button.clicked.connect(self.on_write_click)
        button_layout.addWidget(write_button, alignment=Qt.AlignRight)

        #버튼 레이아웃
        main_layout.addLayout(button_layout)

        self.setLayout(main_layout)
        self.show()

        # 게시판에 초기 텍스트 추가
        self.load_text_from_file("")

        # 경고 메시지
        self.show_warning()

        # 전체 스타일 시트 설정
        self.setStyleSheet("""
        QWidget {
                background-color: #f0f0f0;
            }
            QLabel {
                color: #333;
            }
            QPushButton {
                background-color: #007BFF;
                color: white;
                border-radius: 5px;
                padding: 10px;
            }
            QPushButton:hover {
                background-color: #0056b3;
            }
            QComboBox {
                background-color: white;
                padding: 5px;
            }
            QTextEdit {
                background-color: white;
                border: 1px solid #ccc;
            }
            QCheckBox {
                background-color: #f0f0f0;
            }
        """)

    def update_title_and_load_text(self):
        selected_disease = self.disease_combo.currentText()
        self.title_label.setText(f'({selected_disease}) - 노하우')

        # 새로운 질병 선택 시 해당 파일 읽어오기
        self.load_text_from_file(selected_disease)

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def on_write_click(self):
        selected_disease = self.disease_combo.currentText()
        self.setWindowTitle(f'{selected_disease} - 노하우')

        # 이름 입력 대화 상자에서 이름 받기
        name, ok_pressed = QInputDialog.getText(self, "이름 입력", "이름을 입력하세요:")
        if ok_pressed:
            input_dialog = InputDialog(self)
            if input_dialog.exec_():
                text = input_dialog.text_edit.toPlainText()
                if text.strip():
                    # 작성된 텍스트를 선택한 질병에 해당하는 파일에 저장
                    self.save_text_to_file(selected_disease, name, text)
                    # 저장된 파일을 다시 읽어와 게시판에 표시
                    self.load_text_from_file(selected_disease)
                else:
                    QMessageBox.warning(self, '경고', '텍스트를 입력하세요.')

    def on_prev_click(self):
        self.close()

    def save_text_to_file(self, selected_disease, name, text):
        file_name = f'{selected_disease.replace(" ", "_")}_노하우.txt'
        with open(file_name, 'a', encoding='utf-8') as file:
            file.write(f"{name}: {text}\n")

    def load_text_from_file(self, selected_disease):
        file_name = f'{selected_disease.replace(" ", "_")}_노하우.txt'
        if os.path.exists(file_name):
            with open(file_name, 'r', encoding='utf-8') as file:
                text = file.read()
                self.text_board.setPlainText(text)

    #경고 창
    def show_warning(self):
        QMessageBox.warning(self, '주의', '게시된 내용은 정확하지 않을 수 있습니다. 주의하세요!')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = QuestionWindow()
    sys.exit(app.exec_())


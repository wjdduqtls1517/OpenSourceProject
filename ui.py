import sys
import os
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QRadioButton, QComboBox, QCheckBox, \
    QGridLayout, QPushButton, QDesktopWidget, QStackedWidget, QFrame, QTextEdit, QSpacerItem, QSizePolicy, QMessageBox
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt, QSize


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('My First Application')
        self.resize(800, 1000)
        self.center()

        self.stack = QStackedWidget(self)
        self.first_page = QWidget()
        self.second_page = QWidget()
        self.third_page = QWidget()

        self.initFirstPage()
        self.initSecondPage()
        self.initThirdPage()

        self.stack.addWidget(self.first_page)
        self.stack.addWidget(self.second_page)
        self.stack.addWidget(self.third_page)

        main_layout = QVBoxLayout()
        main_layout.addWidget(self.stack)
        self.setLayout(main_layout)

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

    def initFirstPage(self):
        vbox = QVBoxLayout()

        # 제목 라벨
        title = QLabel('건강관리', self)
        title.setFont(QFont('Noto Sans', 30, QFont.Bold))
        title.setAlignment(Qt.AlignCenter)
        vbox.addWidget(title)

        vbox.addSpacerItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        # 성별 라디오 버튼
        gender_layout = QHBoxLayout()
        gender_label = QLabel('성별을 선택해 주세요.', self)
        gender_label.setFont(QFont('Noto Sans', 16))
        gender_layout.addWidget(gender_label)

        self.male_radio = QRadioButton('남자', self)
        self.male_radio.setFont(QFont('Noto Sans', 16))
        self.female_radio = QRadioButton('여자', self)
        self.female_radio.setFont(QFont('Noto Sans', 16))
        gender_layout.addWidget(self.male_radio)
        gender_layout.addWidget(self.female_radio)
        vbox.addLayout(gender_layout)

        vbox.addSpacerItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        # 나이 콤보박스
        age_layout = QHBoxLayout()
        age_label = QLabel('나이를 선택해 주세요.', self)
        age_label.setFont(QFont('Noto Sans', 16))
        self.age_combo = QComboBox(self)
        self.age_combo.setFont(QFont('Noto Sans', 16))
        self.age_combo.addItem('선택 안함')
        self.age_combo.addItems([f'{i}대' for i in range(60, 90, 10)])
        age_layout.addWidget(age_label)
        age_layout.addWidget(self.age_combo)
        vbox.addLayout(age_layout)

        vbox.addSpacerItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        # 다음 버튼 레이아웃
        button_layout = QHBoxLayout()
        next_button = QPushButton('다음', self)
        next_button.setFont(QFont('Noto Sans', 16))
        next_button.setFixedSize(100, 40)
        next_button.clicked.connect(self.nextPage)
        button_layout.addWidget(next_button, alignment=Qt.AlignRight)
        vbox.addLayout(button_layout)

        self.first_page.setLayout(vbox)

    def initSecondPage(self):
        vbox = QVBoxLayout()

        # 제목 라벨
        title = QLabel('질병 선택', self)
        title.setFont(QFont('Noto Sans', 30, QFont.Bold))
        title.setAlignment(Qt.AlignCenter)
        vbox.addWidget(title)

        vbox.addSpacerItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        # 질병 체크박스 레이아웃
        disease_layout = QGridLayout()
        disease_layout.setSpacing(10)  # 간격을 조정
        disease_layout.setVerticalSpacing(50)  # 행 간격을 매우 넓힘

        self.diseases = [
            '간질환', '갑상선', '고혈압', '골다공증', '관절염', '노인성빈혈',
            '노인성우울증', '녹내장', '뇌동맥류', '뇌졸증', '당뇨병', '동맥경화증',
            '변비', '파킨슨병', '신장병', '오십견', '요통', '위장병', '치매',
            '통풍', '퇴행성근골격장애'
        ]

        self.disease_checkboxes = []
        for i, disease in enumerate(self.diseases):
            checkbox = QCheckBox(disease, self)
            checkbox.setFont(QFont('Noto Sans', 16))
            tooltip_text = self.readDiseaseInfo(os.path.join('diseases', '증상', f'{disease}_증상.txt'))
            checkbox.setToolTip(tooltip_text)
            row = i // 3  # 세로로 3개씩 배치
            col = i % 3  # 가로로 3개씩 배치
            disease_layout.addWidget(checkbox, row, col)
            self.disease_checkboxes.append(checkbox)
        vbox.addLayout(disease_layout)

        vbox.addSpacerItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        # 버튼 레이아웃
        button_layout = QHBoxLayout()
        prev_button = QPushButton('이전', self)
        prev_button.setFont(QFont('Noto Sans', 14))
        prev_button.setFixedSize(100, 40)
        prev_button.clicked.connect(self.prevPage)
        next_button = QPushButton('다음', self)
        next_button.setFont(QFont('Noto Sans', 14))
        next_button.setFixedSize(100, 40)
        next_button.clicked.connect(self.nextPage)
        button_layout.addWidget(prev_button, alignment=Qt.AlignLeft)
        button_layout.addWidget(next_button, alignment=Qt.AlignRight)
        vbox.addLayout(button_layout)

        self.second_page.setLayout(vbox)

    def initThirdPage(self):
        vbox = QVBoxLayout()

        # 사용자 정보 표시
        self.user_info_label = QLabel(self)
        self.user_info_label.setFont(QFont('Noto Sans', 18))
        self.user_info_label.setAlignment(Qt.AlignCenter)
        vbox.addWidget(self.user_info_label)

        # 나의 질병 레이아웃
        my_disease_box = QVBoxLayout()
        my_disease_label = QLabel('나의 질병', self)
        my_disease_label.setFont(QFont('Noto Sans', 16))
        my_disease_label.setAlignment(Qt.AlignCenter)

        self.my_disease_list = QTextEdit(self)
        self.my_disease_list.setFont(QFont('Noto Sans', 14))
        self.my_disease_list.setReadOnly(True)

        my_disease_box.addWidget(my_disease_label)
        my_disease_box.addWidget(self.my_disease_list)

        my_disease_frame = QFrame(self)
        my_disease_frame.setLayout(my_disease_box)
        my_disease_frame.setFrameShape(QFrame.Box)
        vbox.addWidget(my_disease_frame)

        # 알아보기 버튼
        learn_more_button = QPushButton('알아보기', self)
        learn_more_button.setFont(QFont('Noto Sans', 14))
        learn_more_button.setStyleSheet("""
            QPushButton {
                background-color: #007BFF;
                color: white;
                border-radius: 5px;
                padding: 10px;
            }
            QPushButton:hover {
                background-color: #0056b3;
            }
        """)
        learn_more_button.setFixedSize(learn_more_button.sizeHint())
        my_disease_box.addWidget(learn_more_button, alignment=Qt.AlignRight)

        # 조심해야 할 병 레이아웃
        caution_disease_box = QVBoxLayout()
        caution_disease_label = QLabel('조심해야 할 병', self)
        caution_disease_label.setFont(QFont('Noto Sans', 16))
        caution_disease_label.setAlignment(Qt.AlignCenter)

        self.caution_disease_list = QTextEdit(self)
        self.caution_disease_list.setFont(QFont('Noto Sans', 14))
        self.caution_disease_list.setReadOnly(True)

        caution_disease_box.addWidget(caution_disease_label)
        caution_disease_box.addWidget(self.caution_disease_list)

        caution_disease_frame = QFrame(self)
        caution_disease_frame.setLayout(caution_disease_box)
        caution_disease_frame.setFrameShape(QFrame.Box)
        vbox.addWidget(caution_disease_frame)

        # 더 알아보기 버튼
        learn_more_caution_button = QPushButton('알아보기', self)
        learn_more_caution_button.setFont(QFont('Noto Sans', 14))
        learn_more_caution_button.setStyleSheet("""
            QPushButton {
                background-color: #007BFF;
                color: white;
                border-radius: 5px;
                padding: 10px;
            }
            QPushButton:hover {
                background-color: #0056b3;
            }
        """)
        learn_more_caution_button.setFixedSize(learn_more_caution_button.sizeHint())
        caution_disease_box.addWidget(learn_more_caution_button, alignment=Qt.AlignRight)

        # 버튼 레이아웃
        button_layout = QHBoxLayout()
        prev_button = QPushButton('이전', self)
        prev_button.setFont(QFont('Noto Sans', 14))
        prev_button.setFixedSize(100, 40)
        prev_button.clicked.connect(self.prevPage)
        next_button = QPushButton('완료', self)  # 완료 버튼으로 변경
        next_button.setFont(QFont('Noto Sans', 14))
        next_button.setFixedSize(100, 40)
        next_button.clicked.connect(self.displayUserInfo)
        button_layout.addWidget(prev_button, alignment=Qt.AlignLeft)
        button_layout.addWidget(next_button, alignment=Qt.AlignRight)
        vbox.addLayout(button_layout)

        self.third_page.setLayout(vbox)

    def nextPage(self):
        current_index = self.stack.currentIndex()
        if current_index == 0:
            # 첫 번째 페이지 유효성 검사
            if not self.male_radio.isChecked() and not self.female_radio.isChecked():
                QMessageBox.warning(self, '입력 오류', '성별을 선택해 주세요.')
                return


    def prevPage(self):
        current_index = self.stack.currentIndex()
        if current_index > 0:
            self.stack.setCurrentIndex(current_index - 1)

    def displayUserInfo(self):
        # 사용자 정보 표시
        gender = '남자' if self.male_radio.isChecked() else '여자'
        age = self.age_combo.currentText()
        self.user_info_label.setText(f'성별: {gender}, 나이: {age}')

        # 선택한 질병 목록 표시
        selected_diseases = [checkbox.text() for checkbox in self.disease_checkboxes if checkbox.isChecked()]
        self.my_disease_list.setText('\n'.join(selected_diseases))

        # 조심해야 할 병 (예시로 두 번째 질병을 표시)
        if len(selected_diseases) > 1:
            self.caution_disease_list.setText(selected_diseases[1])
        else:
            self.caution_disease_list.clear()

    def readDiseaseInfo(self, file_path):
        if not os.path.exists(file_path):
            return ''
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    ex.show()
    sys.exit(app.exec_())


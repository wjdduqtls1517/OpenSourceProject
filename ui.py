import sys
import os
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QRadioButton, QComboBox, QCheckBox, \
    QGridLayout, QPushButton, QDesktopWidget, QStackedWidget, QFrame, QTextEdit
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

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

    def initFirstPage(self):
        vbox = QVBoxLayout()

        # 제목 라벨
        title = QLabel('건강관리', self)
        title.setFont(QFont('Noto Sans', 30, QFont.Bold))
        title.setAlignment(Qt.AlignCenter)
        vbox.addWidget(title)

        # 성별 라디오 버튼
        gender_layout = QHBoxLayout()
        gender_label = QLabel('성별', self)
        gender_label.setFont(QFont('Noto Sans', 14))
        gender_layout.addWidget(gender_label)

        self.male_radio = QRadioButton('남자', self)
        self.male_radio.setFont(QFont('Noto Sans', 14))
        self.female_radio = QRadioButton('여자', self)
        self.female_radio.setFont(QFont('Noto Sans', 14))
        gender_layout.addWidget(self.male_radio)
        gender_layout.addWidget(self.female_radio)
        vbox.addLayout(gender_layout)

        # 나이 콤보박스
        age_layout = QHBoxLayout()
        age_label = QLabel('나이', self)
        age_label.setFont(QFont('Noto Sans', 14))
        self.age_combo = QComboBox(self)
        self.age_combo.setFont(QFont('Noto Sans', 14))
        self.age_combo.addItem('선택 안함')
        self.age_combo.addItems([f'{i}대' for i in range(60, 90, 10)])
        age_layout.addWidget(age_label)
        age_layout.addWidget(self.age_combo)
        vbox.addLayout(age_layout)

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

        self.first_page.setLayout(vbox)

    def initSecondPage(self):
        vbox = QVBoxLayout()

        # 제목 라벨
        title = QLabel('질병 선택', self)
        title.setFont(QFont('Noto Sans', 30, QFont.Bold))
        title.setAlignment(Qt.AlignCenter)
        vbox.addWidget(title)

        # 질병 체크박스 레이아웃
        disease_layout = QGridLayout()
        self.diseases = [
            '간질환', '갑상선', '고혈압', '골다공증', '관절염', '노인성빈혈',
            '노인성우울증', '녹내장', '뇌동맥류', '뇌졸증', '당뇨병', '동맥경화증',
            '변비', '파킨슨병', '신장병', '오십견', '요통', '위장병', '치매',
            '통풍', '퇴행성근골격장애'
        ]

        self.disease_checkboxes = []
        for i, disease in enumerate(self.diseases):
            checkbox = QCheckBox(disease, self)
            checkbox.setFont(QFont('Noto Sans', 14))
            if disease == '간질환':
                tooltip_text = self.readDiseaseInfo(os.path.join('diseases', '증상', '간질환_증상.txt'))
                checkbox.setToolTip(tooltip_text)
            row = i // 7
            col = i % 7
            disease_layout.addWidget(checkbox, row, col)
            self.disease_checkboxes.append(checkbox)
        vbox.addLayout(disease_layout)

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
        learn_more_button.setFixedSize(100, 40)
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
        learn_more_caution_button = QPushButton('더 알아보기', self)
        learn_more_caution_button.setFont(QFont('Noto Sans', 14))
        learn_more_caution_button.setFixedSize(120, 40)
        caution_disease_box.addWidget(learn_more_caution_button, alignment=Qt.AlignRight)

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

        self.third_page.setLayout(vbox)

    def readDiseaseInfo(self, filepath):
        try:
            with open(filepath, 'r', encoding='utf-8') as file:
                return file.read()
        except Exception as e:
            return f'파일을 읽는 중 오류가 발생했습니다: {e}'

    def prevPage(self):
        current_index = self.stack.currentIndex()
        if current_index > 0:
            self.stack.setCurrentIndex(current_index - 1)

    def nextPage(self):
        current_index = self.stack.currentIndex()
        if current_index == 0:
            self.updateUserInfo()
        elif current_index == 1:
            self.updateThirdPage()
        if current_index < self.stack.count() - 1:
            self.stack.setCurrentIndex(current_index + 1)

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def updateUserInfo(self):
        gender = '남자' if self.male_radio.isChecked() else '여자' if self.female_radio.isChecked() else '성별 없음'
        age = self.age_combo.currentText()
        self.user_info_label.setText(f'성별: {gender}, 나이: {age}')

    def updateThirdPage(self):
        selected_diseases = [checkbox.text() for checkbox in self.disease_checkboxes if checkbox.isChecked()]
        self.my_disease_list.setText('\n'.join(selected_diseases))

        age = self.age_combo.currentText()
        if age == '60대':
            caution_diseases = self.diseases[:5]
        elif age == '70대':
            caution_diseases = self.diseases[5:10]
        elif age == '80대':
            caution_diseases = self.diseases[10:15]
        else:
            caution_diseases = []

        self.caution_disease_list.setText('\n'.join(caution_diseases))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    ex.show()
    sys.exit(app.exec_())

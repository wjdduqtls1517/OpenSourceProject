import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QRadioButton, QComboBox, QCheckBox, \
    QGridLayout, QPushButton, QDesktopWidget, QStackedWidget
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

        self.initFirstPage()
        self.initSecondPage()

        self.stack.addWidget(self.first_page)
        self.stack.addWidget(self.second_page)

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
        diseases = [
            '간질환', '갑상선', '고혈압', '골다공증', '관절염', '노인성빈혈',
            '노인성우울증', '녹내장', '뇌동맥류', '뇌졸증', '당뇨병', '동맥경화증',
            '변비', '파킨슨병', '신장병', '오십견', '요통', '위장병', '치매',
            '통풍', '퇴행성근골격장애'
        ]
        disease_info = [
            '간질환 정보', '갑상선 정보', '고혈압 정보', '골다공증 정보', '관절염 정보',
            '노인성빈혈 정보', '노인성우울증 정보', '녹내장 정보', '뇌동맥류 정보', '뇌졸증 정보',
            '당뇨병 정보', '동맥경화증 정보', '변비 정보', '파킨슨병 정보', '신장병 정보',
            '오십견 정보', '요통 정보', '위장병 정보', '치매 정보', '통풍 정보',
            '퇴행성근골격장애 정보'
        ]

        for i, disease in enumerate(diseases):
            checkbox = QCheckBox(disease, self)
            checkbox.setFont(QFont('Noto Sans', 14))
            checkbox.setToolTip(disease_info[i])
            row = i // 7
            col = i % 7
            disease_layout.addWidget(checkbox, row, col)
        vbox.addLayout(disease_layout)

        # 버튼 레이아웃
        button_layout = QHBoxLayout()
        prev_button = QPushButton('이전', self)
        prev_button.setFont(QFont('Noto Sans', 14))
        prev_button.setFixedSize(100, 40)
        prev_button.clicked.connect(self.prevPage)
        button_layout.addWidget(prev_button, alignment=Qt.AlignLeft)
        vbox.addLayout(button_layout)

        self.second_page.setLayout(vbox)

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def nextPage(self):
        self.stack.setCurrentWidget(self.second_page)

    def prevPage(self):
        self.stack.setCurrentWidget(self.first_page)

    def exit_application(self):
        QApplication.instance().quit()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    ex.show()
    sys.exit(app.exec_())

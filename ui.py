import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QRadioButton, QComboBox, QCheckBox, QGridLayout, QPushButton, QDesktopWidget, QStackedWidget
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('My First Application')
        self.resize(800, 1000)  # 창 크기 조정
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
        gender_label.setFont(QFont('Noto Sans', 14))  # 폰트 크기 조정
        gender_layout.addWidget(gender_label)

        self.male_radio = QRadioButton('남자', self)
        self.male_radio.setFont(QFont('Noto Sans', 14))  # 폰트 크기 조정
        self.female_radio = QRadioButton('여자', self)
        self.female_radio.setFont(QFont('Noto Sans', 14))  # 폰트 크기 조정
        gender_layout.addWidget(self.male_radio)
        gender_layout.addWidget(self.female_radio)
        vbox.addLayout(gender_layout)

        # 나이 콤보박스
        age_layout = QHBoxLayout()
        age_label = QLabel('나이', self)
        age_label.setFont(QFont('Noto Sans', 14))  # 폰트 크기 조정
        self.age_combo = QComboBox(self)
        self.age_combo.setFont(QFont('Noto Sans', 14))  # 폰트 크기 조정
        self.age_combo.addItem('선택 안함')
        self.age_combo.addItems([f'{i}대' for i in range(60, 90, 10)])
        age_layout.addWidget(age_label)
        age_layout.addWidget(self.age_combo)
        vbox.addLayout(age_layout)

        # 버튼 레이아웃
        button_layout = QHBoxLayout()
        prev_button = QPushButton('이전', self)
        prev_button.setFont(QFont('Noto Sans', 14))  # 폰트 크기 조정
        prev_button.setFixedSize(100, 40)  # 버튼 크기 조정
        prev_button.clicked.connect(self.prevPage)
        next_button = QPushButton('다음', self)
        next_button.setFont(QFont('Noto Sans', 14))  # 폰트 크기 조정
        next_button.setFixedSize(100, 40)  # 버튼 크기 조정
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
        diseases = [f'질병 {i}' for i in range(1, 22)]
        for i, disease in enumerate(diseases):
            checkbox = QCheckBox(disease, self)
            checkbox.setFont(QFont('Noto Sans', 14))  # 폰트 크기 조정
            row = i // 7
            col = i % 7
            disease_layout.addWidget(checkbox, row, col)
        vbox.addLayout(disease_layout)

        # 버튼 레이아웃
        button_layout = QHBoxLayout()
        prev_button = QPushButton('이전', self)
        prev_button.setFont(QFont('Noto Sans', 14))  # 폰트 크기 조정
        prev_button.setFixedSize(100, 40)  # 버튼 크기 조정
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

# 입력 버튼
        write_button = QPushButton('작성', self)
        write_button.setFont(QFont('Noto Sans', 16))
        write_button.setFixedSize(100, 40)
        write_button.setStyleSheet("background-color: blue; color: white;")
        write_button.clicked.connect(self.on_write_click)
        button_layout.addWidget(write_button, alignment=Qt.AlignRight)


# 이전 버튼
        prev_button = QPushButton('이전', self)
        prev_button.setFont(QFont('Noto Sans', 16))
        prev_button.setFixedSize(100, 40)
        prev_button.setStyleSheet("background-color: blue; color: white;")
        prev_button.clicked.connect(self.on_prev_click)  # 이전 버튼 클릭 시 처리할 슬롯 연결
        button_layout.addWidget(prev_button, alignment=Qt.AlignLeft)

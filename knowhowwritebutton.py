  #노하우 작성 확인 버튼
        confirm_button = QPushButton('확인')
        confirm_button.setFont(font_button)
        confirm_button.clicked.connect(self.accept)
        layout.addWidget(confirm_button)

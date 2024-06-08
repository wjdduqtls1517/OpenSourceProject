   # 텍스트 게시판
        self.text_board = QTextEdit(self)
        self.text_board.setFont(font_label)
        self.text_board.setReadOnly(True)
        main_layout.addWidget(self.text_board)


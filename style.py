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

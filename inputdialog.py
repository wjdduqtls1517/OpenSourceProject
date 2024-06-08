class InputDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('노하우 작성')
        self.text_edit = QTextEdit()

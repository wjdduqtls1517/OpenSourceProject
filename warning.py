import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox
from PyQt5.QtCore import Qt

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Main Window')
        self.setGeometry(100, 100, 300, 200)

        # 경고 대화 상자 띄우기
        QMessageBox.warning(self, '주의', '개시된 내용은 정확하지 않을 수 있으니, 주의하세요!')

if __name__ == '__main__':
    app = QApplication(sys.argv)

    # 메인 윈도우 생성
    main_window = MainWindow()
    main_window.show()

    # 어플리케이션 실행
    sys.exit(app.exec_())


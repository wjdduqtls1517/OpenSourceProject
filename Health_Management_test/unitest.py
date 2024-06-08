import unittest
from PyQt5.QtWidgets import QApplication, QMessageBox
from PyQt5.QtCore import Qt
from myapp import MyApp

class TestMyApp(unittest.TestCase):
    def setUp(self):
        self.app = QApplication([])
        self.window = MyApp()

    def test_nextPage_without_gender_age(self):
        next_button = self.window.first_page.findChild(QPushButton, 'next_button')
        next_button.click()  # "다음" 버튼 클릭
        self.assertEqual(self.window.stack.currentIndex(), 0)  # 페이지 전환되지 않음을 확인

        # 경고 메시지 확인
        warning_dialog = self.window.findChild(QMessageBox)
        self.assertEqual(warning_dialog.text(), '입력 오류')
        self.assertEqual(warning_dialog.informativeText(), '성별을 선택해 주세요.')

    def tearDown(self):
        self.window.close()

if __name__ == '__main__':
    unittest.main()

import unittest
from PyQt5.QtTest import QTest
from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtWidgets import QApplication, QPushButton, QTextEdit

from knowhow1 import QuestionWindow, InputDialog  # 테스트할 모듈을 임포트합니다.

app = QApplication([])  # 전역적으로 한 번만 QApplication을 생성합니다.


class TestQuestionWindow(unittest.TestCase):
    def setUp(self):
        self.widget = QuestionWindow()

    def tearDown(self):
        self.widget.close()

    def test_window_title(self):
        self.assertEqual(self.widget.windowTitle(), '질병 - 노하우')

    def test_combo_box_initial_state(self):
        self.assertEqual(self.widget.disease_combo.currentText(), '간질환')
        self.assertEqual(self.widget.disease_combo.count(), 21)  # 총 21개의 항목이 있는지 확인합니다.

    def test_text_board_initial_state(self):
        self.assertTrue(self.widget.text_board.toPlainText() == '')

    def test_update_title_and_load_text(self):
        QTest.mouseClick(self.widget.disease_combo.view().indexAt(QPoint(0, 1)), Qt.LeftButton)  # 첫 번째 항목을 클릭합니다.
        self.assertEqual(self.widget.title_label.text(), '(간질환) - 노하우')

    def test_on_write_click(self):
        write_button = self.widget.findChild(QPushButton, '작성')
        QTest.mouseClick(write_button, Qt.LeftButton)

        input_dialog = self.widget.findChild(InputDialog)
        self.assertIsNotNone(input_dialog)  # InputDialog 창이 열렸는지 확인합니다.

        QTest.keyClicks(input_dialog.findChild(QTextEdit), 'This is a test.')
        confirm_button = input_dialog.findChild(QPushButton, '확인')
        QTest.mouseClick(confirm_button, Qt.LeftButton)

        self.assertIn('This is a test.', self.widget.text_board.toPlainText())


if __name__ == '__main__':
    unittest.main()


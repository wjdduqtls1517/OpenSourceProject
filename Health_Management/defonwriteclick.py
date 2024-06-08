    def on_write_click(self):
        selected_disease = self.disease_combo.currentText()
        self.setWindowTitle(f'{selected_disease} - 노하우')

        # 이름 입력 대화 상자에서 이름 받기
        name, ok_pressed = QInputDialog.getText(self, "이름 입력", "이름을 입력하세요:")
        if ok_pressed:
            input_dialog = InputDialog(self)
            if input_dialog.exec_():
                text = input_dialog.text_edit.toPlainText()
                if text.strip():
                    # 작성된 텍스트를 선택한 질병에 해당하는 파일에 저장
                    self.save_text_to_file(selected_disease, name, text)
                    # 저장된 파일을 다시 읽어와 게시판에 표시
                    self.load_text_from_file(selected_disease)
                else:
                    QMessageBox.warning(self, '경고', '텍스트를 입력하세요.')


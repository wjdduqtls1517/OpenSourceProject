    def update_title_and_load_text(self):
        selected_disease = self.disease_combo.currentText()
        self.title_label.setText(f'({selected_disease}) - 노하우')

        # 새로운 질병 선택 시 해당 파일 읽어오기
        self.load_text_from_file(selected_disease)


    def load_text_from_file(self, selected_disease):
        file_name = f'{selected_disease.replace(" ", "_")}_노하우.txt'
        if os.path.exists(file_name):
            with open(file_name, 'r', encoding='utf-8') as file:
                text = file.read()
                self.text_board.setPlainText(text)


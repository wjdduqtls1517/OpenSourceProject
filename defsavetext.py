    def save_text_to_file(self, selected_disease, name, text):
        file_name = f'{selected_disease.replace(" ", "_")}_노하우.txt'
        with open(file_name, 'a', encoding='utf-8') as file:
            file.write(f"{name}: {text}\n")

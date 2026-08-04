# database.py
# Tudo relacionado aos arquivos.

# Exemplo:
# load_tasks()
# save_tasks(tasks)
# create_database_if_not_exists()
# backup_database()

# Esse arquivo não sabe o que é uma interface gráfica.
# Só lê e grava dados.

import json

from models import Task

class Database:
    def __init__(self):
        self.file_path = "data/tasks.json"
        
    def next_id(self):
        print()

    def load_tasks(self):
        try:
            with open(self.file_path, "r", encoding="utf-8") as file:
                data = json.load(file)
        except FileNotFoundError:
            print("Erro ao Abrir o arquivo!")
            return []

        tasks = []

        for task in data:
            tasks.append(Task(**task))

        return tasks

    def save_task(self, tasks):
        with open(self.file_path, "w", encoding="utf-8") as file:
            json.dump(tasks, file, ensure_ascii=False, indent=4)
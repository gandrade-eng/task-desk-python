# Exemplo:
# load_tasks()
# save_tasks(tasks)
# create_database_if_not_exists()
# backup_database()


# if not os.path.exists(self.history_path):
#     with open(self.history_path, "w", encoding="utf-8") as file:
#         json.dump([], file)

# external imports
import json
# internal imports
from models import Task

class Database:
    def __init__(self):
        self.tasks_path = "data/tasks.json"
        self.history_path = "data/history.json"

    # Tasks
    # //////////////////////////////////////////////////////////
    def load_tasks(self):
        try:
            with open(self.tasks_path, "r", encoding="utf-8") as file:
                data = json.load(file)
        except FileNotFoundError:
            print("Erro ao Abrir o arquivo tasks!")
            return []
        except json.JSONDecodeError:
            print("está vazio ou contém JSON inválido.")
            return []

        tasks = []

        for task in data:
            tasks.append(Task.from_dict(task))

        return tasks

    def save_tasks(self, tasks):
        tasks_data = [task.to_dict() for task in tasks]

        with open(self.tasks_path, "w", encoding="utf-8") as file:
            json.dump(tasks_data, file, ensure_ascii=False, indent=4)

    # History
    # //////////////////////////////////////////////////////////
    def load_history(self):
        try:
            with open(self.history_path, "r", encoding="utf-8") as file:
                data = json.load(file)
        except FileNotFoundError:
            print("Erro ao Abrir o arquivo history!")
            return []
        except json.JSONDecodeError:
            print("está vazio ou contém JSON inválido.")
            return []

        tasks = []

        for task in data:
            tasks.append(Task.from_dict(task))

        return tasks 

    def save_history(self, tasks):
        tasks_data = [task.to_dict() for task in tasks]

        with open(self.history_path, "w", encoding="utf-8") as file:
            json.dump(tasks_data, file, ensure_ascii=False, indent=4)


# def to_dict(self):

# @classmethod
# def from_dict(cls, data):
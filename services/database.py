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

def loadTasks():
    try:
        with open("data/tasks.json", "r", encoding="utf-8") as file:
            tasks = json.load(file)
    except FileNotFoundError:
        tasks = []
    return tasks

def saveTask(tasks):
    with open("data/tasks.json", "w", encoding="utf-8") as file:
        json.dump(tasks, file, ensure_ascii=False, indent=4)
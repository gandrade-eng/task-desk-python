# lógica de carregar/salvar JSON

import json

def loadSettings():
    try:
        with open("data/settings.json", "r", encoding="utf-8") as file:
            settings = json.load(file)
    except FileNotFoundError:
            settings = []
    return settings

def saveSettings():
    # with open("data/tasks.json", "w", encoding="utf-8") as file:
    #     json.dump(tasks, file, ensure_ascii=False, indent=4)
    print()
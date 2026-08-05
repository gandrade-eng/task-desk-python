# lógica de carregar/salvar JSON
import json

class SettingsManager:
    def load_settings():
        try:
            with open("data/settings.json", "r", encoding="utf-8") as file:
                settings = json.load(file)
        except FileNotFoundError:
                settings = []
        return settings

    def save_settings(new_settings):
        with open("data/settings.json", "w", encoding="utf-8") as file:
            json.dump(new_settings, file, ensure_ascii=False, indent=4)
        print("save")
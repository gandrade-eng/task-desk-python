# lógica de carregar/salvar JSON
import json

class SettingsManager:

    @staticmethod
    def load_settings():
        try:
            with open("data/settings.json", "r", encoding="utf-8") as file:
                settings = json.load(file)
        except FileNotFoundError:
                settings = {
                    "theme": "light",
                    "language": "pt",
                    "notifications": True
                }
        return settings

    @staticmethod
    def save_settings(new_settings):
        with open("data/settings.json", "w", encoding="utf-8") as file:
            json.dump(new_settings, file, ensure_ascii=False, indent=4)
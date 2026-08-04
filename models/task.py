# Aqui eu faria as classes do projeto.

# Depois pode adicionar:
# data de criação
# prioridade
# categoria
# prazo
# descrição

from PySide6.QtCore import QDate, QTime

class Task:
    def __init__(self, id, title, description, date, time, completed = False):
        self.id = id
        self.title = title
        self.date = date
        self.time = time
        self.description = description
        self.completed = completed

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "date": self.date.toString("yyyy-MM-dd"),
            "time": self.time.toString("HH:mm"),
            "completed": self.completed
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            id = data["id"],
            title = data["title"],
            description = data["description"],
            date = QDate.fromString(data["date"], "yyyy-MM-dd"),
            time = QTime.fromString(data["time"], "HH:mm"),
            completed = data["completed"]
        )
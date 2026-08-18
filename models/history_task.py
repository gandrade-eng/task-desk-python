from PySide6.QtCore import QDate, QTime

class HistoryTask:
    def __init__(self, id, title, description, date, time, is_completed = False, is_deleted = False):
        self.id = id
        self.title = title
        self.date = date
        self.time = time
        self.description = description
        self.is_completed = is_completed
        self.is_deleted = is_deleted

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "date": self.date.toString("yyyy-MM-dd"),
            "time": self.time.toString("HH:mm"),
            "is_completed": self.is_completed,
            "is_deleted": self.is_deleted
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            id = data["id"],
            title = data["title"],
            description = data["description"],
            date = QDate.fromString(data["date"], "yyyy-MM-dd"),
            time = QTime.fromString(data["time"], "HH:mm"),
            is_completed = data["is_completed"],
            is_deleted = data["is_deleted"]
        )
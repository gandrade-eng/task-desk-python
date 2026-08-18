# external imports
from datetime import datetime, date
# internal imports
from config import LANGUAGES
from models import HistoryTask

# "active"
# "completed"
# "deleted"

# tasks.json contém apenas as "active" e, se você preferir, também as "completed" que ainda não foram removidas.
# history.json contém todas.

class HistoryManager:
    def __init__ (self, database):
        self.database = database
        self.tasks = database.load_history()

    # Getters
    # //////////////////////////////////////////////////////////
    def get_tasks(self):
        return self.tasks
    
    def get_task_statistics(self, tasks):
        total = len(tasks)

        completed = sum(task.is_completed for task in tasks)

        incomplete = total - completed

        return {
            "total": total,
            "completed": completed,
            "incomplete": incomplete
        }
    
    def get_task_completion_percentage(self, tasks):
        stats = self.get_task_statistics(tasks)

        if stats["total"] == 0:
            return 0

        return int((stats["completed"] / stats["total"]) * 100)

    # Helpers
    # //////////////////////////////////////////////////////////
    def next_id(self):
        if not self.tasks:
            return 1
        return max(history.id for history in self.tasks) + 1

    # Actions
    # //////////////////////////////////////////////////////////
    def add_history(self, new_task):
            history_task = HistoryTask(
                new_task.id,
                new_task.title,
                new_task.description,
                new_task.date,
                new_task.time,
                new_task.is_completed,
                False
            )
            self.tasks.append(history_task)
    
            # Saving the file
            self.database.save_history(self.tasks)
    
            # try / except ValueError:
            # date_str = input(LANGUAGES[language]["addTaskDate"])
            # due_date = datetime.strptime(date_str, "%d/%m/%Y")

    def mark_as_deleted(self, task_id):
        for task in self.tasks:
            if task.id == task_id:
                task.is_deleted = True
                break

        # Saving the file
        self.database.save_history(self.tasks)

    # def update_history():

    # def mark_deleted():
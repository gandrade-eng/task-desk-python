# external imports
from datetime import datetime, date
# internal imports
from config import LANGUAGES
from models import Task

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

        completed = sum(task.completed for task in tasks)

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
            self.tasks.append(new_task)
    
            # Saving the file
            self.database.save_history(self.tasks)
    
            # try / except ValueError:
            # date_str = input(LANGUAGES[language]["addTaskDate"])
            # due_date = datetime.strptime(date_str, "%d/%m/%Y")

    # def update_history():

    # def mark_deleted():
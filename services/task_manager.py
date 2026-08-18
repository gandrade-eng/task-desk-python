# external imports
from PySide6.QtCore import QDate
# internal imports
from config import LANGUAGES
from models import Task

# today = datetime.today()
# if date < today:
#     print("Essa tarefa está atrasada!")

# Add Id

class TaskManager:
    def __init__ (self, database, history_manager):
        self.database = database
        self.tasks = database.load_tasks()
        self.history_manager = history_manager

    # Getters
    # //////////////////////////////////////////////////////////
    def get_tasks(self):
        return self.tasks

    def get_today_tasks(self):
        today = QDate.currentDate()

        today_tasks = []

        for task in self.tasks:
            if task.date == today:
                today_tasks.append(task)

        return today_tasks

    def get_upcoming_tasks(self, limit):
        today = QDate.currentDate()
        
        upcoming_tasks = []

        for task in self.tasks:
            if task.date > today:
                upcoming_tasks.append(task)

        upcoming_tasks.sort(key=lambda task: task.date)

        if limit is not None:
            return upcoming_tasks[:limit]

        return upcoming_tasks

    def get_task_statistics(self, tasks):
        total = len(tasks)

        completed = sum(task.is_completed for task in tasks)

        incomplete = total - completed

        return {
            "total": total,
            "completed": completed,
            "incomplete": incomplete
        }

    # IMCOMPLETE
    def get_tasks_created_by_month(self):
        return {
            "january": 1,
            "february": 2,
            "march": 3,
            "april": 4,
            "may": 5,
            "june": 5,
            "july": 5,
            "august": 6,
            "september": 7,
            "october": 2,
            "november": 1,
            "december": 3
        }
    

    # Actions
    # //////////////////////////////////////////////////////////
    def add_task(self, title, date, time, description, is_completed):
        new_task = Task(
            id = self.history_manager.next_id(),
            title = title,
            date = date,
            time = time,
            description = description,
            is_completed = is_completed
        )

        self.tasks.append(new_task)

        # Saving tasks
        self.database.save_tasks(self.tasks)

        return new_task

        # try / except ValueError:
        # date_str = input(LANGUAGES[language]["addTaskDate"])
        # due_date = datetime.strptime(date_str, "%d/%m/%Y")
            
    def remove_task(self, task_id):
        for i, task in enumerate(self.tasks):
            if task.id == task_id:
                self.tasks.pop(i)
                break

        # Saving the file
        self.database.save_tasks(self.tasks)

    # def edit_task(self, taks):
    #     print()

    # def complete_task(tasks):
    #     # Saving the file
    #     Database.save_tasks(tasks)
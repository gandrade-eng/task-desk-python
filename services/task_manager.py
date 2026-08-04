# external imports
from datetime import datetime
# internal imports
from config import LANGUAGES
from services import Database

# today = datetime.today()
# if date < today:
#     print("Essa tarefa está atrasada!")

# Add Id

class TaskManager:
    def __init__ (self, tasks):
        self.tasks = tasks

    def add_task(self, newTask):
        self.tasks.append(newTask)

        # try / except ValueError:
        # date_str = input(LANGUAGES[language]["addTaskDate"])
        # due_date = datetime.strptime(date_str, "%d/%m/%Y")

        # Saving the file
        Database.save_task(self.tasks)
            
    def remove_task(self, task_id):
        for i, task in enumerate(self.tasks):
            if task["id"] == task_id:
                self.tasks.pop(i)
                break

        # Saving the file
        Database.save_task(self.tasks)

    # def edit_task(self, taks):
    #     print()

    # def complete_task(tasks):
    #     # Saving the file
    #     Database.save_task(tasks)
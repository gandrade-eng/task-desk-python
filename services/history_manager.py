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
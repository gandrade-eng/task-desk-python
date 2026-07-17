# external imports
from datetime import datetime
# internal imports
from ui.settings import LANGUAGES, language
from services.database import saveTask

# today = datetime.today()
# if date < today:
#     print("Essa tarefa está atrasada!")

def addTask(tasks):
    task_title = input(LANGUAGES[language]["addTask"])

    while True:
        try:
            date_str = input(LANGUAGES[language]["addTaskDate"])
            due_date = datetime.strptime(date_str, "%d/%m/%Y")
            break
        except ValueError:
            print(LANGUAGES[language]["addTaskDateError"])

    newTask = {
        "title": task_title,
        "completed": False,
        "date": due_date.strftime("%d/%m/%Y")
    }
    tasks.append(newTask)

    # Saving the file
    saveTask(tasks)

def listTasks(tasks):
    # for task in tasks: print(task)
    # for i in range(len(tasks))
    # ☐ ☑
    if not tasks:
        print(LANGUAGES[language]["listTasksEmpty"])
        return
    
    print(LANGUAGES[language]["listTasks"])

    for i, task in enumerate(tasks, start = 1):
        status = "X" if task['completed'] else " "
        print(f"{i} [{status}] {task['title']}")
        
def removeTask(tasks):
    for i in range(len(tasks)):
        print(f"{i+1} - {tasks[i]['title']}")
    print()

    choiceTask = int(input(LANGUAGES[language]["removeTask"]))
    tasks.pop(choiceTask-1)

    # Saving the file
    saveTask(tasks)

def completeTask(tasks):
    for i in range(len(tasks)):
        if not tasks[i]["completed"]:
            print(f"{i+1} - {tasks[i]['title']}")

    choiceCompleteTask = int(input(LANGUAGES[language]["completeTask"]))
    tasks[choiceCompleteTask-1]["completed"] = True

    # Saving the file
    saveTask(tasks)
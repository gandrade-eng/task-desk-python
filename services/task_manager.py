from ui.settings import LANGUAGES, language
from services.database import saveTask

def addTask(tasks):
    task = input(LANGUAGES[language]["addTask"])
    date = input(LANGUAGES[language]["addTaskDate"])
    newTask = {
        "title": task,
        "completed": False,
        "date": date
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
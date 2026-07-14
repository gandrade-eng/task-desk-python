from ui.settings import LANGUAGES, language
# import ui.settings

tasks = []

def addTask():
    task = input(LANGUAGES[language]["addTask"])
    newTask = {
        "title": task,
        "completed": False
    }
    tasks.append(newTask)

def listTasks():
    # for task in tasks: print(task)
    # ☐ ☑
    print(LANGUAGES[language]["listTasks"])
    for i in range(len(tasks)):
        print(
            f"[{("X" if tasks[i]['completed'] else " ")}] " 
            f"{tasks[i]["title"]}"
        )
        
def removeTask():
    for i in range(len(tasks)):
        print(f"{i+1} - {tasks[i]['title']}")
    print()

    choiceTask = int(input(LANGUAGES[language]["removeTask"]))
    tasks.pop(choiceTask-1)

def completeTask():
    for i in range(len(tasks)):
        if not tasks[i]["completed"]:
            print(f"{i+1} - {tasks[i]['title']}")

    choiceCompleteTask = int(input(LANGUAGES[language]["completeTask"]))
    tasks[choiceCompleteTask-1]["completed"] = True

def main ():
    print(LANGUAGES[language]["welcome"])
    while(True):
        print(LANGUAGES[language]["menu"])
        print(LANGUAGES[language]["menuChoices"])
        choice = int(input(LANGUAGES[language]["choice"]))

        match choice:
            case 1:
                print()
                addTask()
                print()
            case 2:
                print()
                listTasks()
                print()
            case 3:
                print()
                removeTask()
                print()
            case 4:
                print()
                completeTask()
                print()
            case 5:
                print(LANGUAGES[language]["exit"])
                break

if __name__ == "__main__":
    main()
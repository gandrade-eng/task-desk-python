# import ui.settings
from ui.settings import LANGUAGES, language
from services.database import loadTasks
from services.task_manager import addTask, listTasks, removeTask, completeTask

def main ():
    # Loading the File
    tasks = loadTasks()

    print(LANGUAGES[language]["welcome"])
    while(True):
        print(LANGUAGES[language]["menu"])
        print(LANGUAGES[language]["menuChoices"])
        choice = int(input(LANGUAGES[language]["choice"]))

        match choice:
            case 1:
                print()
                addTask(tasks)
                print()
            case 2:
                print()
                listTasks(tasks)
                print()
            case 3:
                print()
                removeTask(tasks)
                print()
            case 4:
                print()
                completeTask(tasks)
                print()
            case 5:
                print(LANGUAGES[language]["exit"])
                break

if __name__ == "__main__":
    main()
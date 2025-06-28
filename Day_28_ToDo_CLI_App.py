#Day_28 <Practice Project - To Do CLI App>
#- Add, Delete, Mark tasks
#- Store in a JSON or text file

import json
import os
from colorama import Fore,Style, init

init(autoreset=True) #for automatic reset after color

FILE_NAME = "tasks.json"

def load_tasks():
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, 'r') as f:
        return json.load(f)

def save_tasks(tasks):
    with open(FILE_NAME, 'w') as f:
        json.dump(tasks, f, indent=4)

def show_tasks(tasks):
    if not tasks:
        print(Fore.YELLOW + "No tasks found.")
        return

    # Sort tasks: not done first
    tasks_sorted = sorted(tasks, key=lambda x: x['done'])

    for i, task in enumerate(tasks_sorted, start=1):
        status = Fore.GREEN + "✅" if task["done"] else Fore.RED + "❌"
        due = task.get("due", "No due date")
        print(f"{i}. {task['task']} [{status}{Style.RESET_ALL}] - Due: {due}")

def add_task(tasks):
    task = input("Enter task description: ")
    due_date = input("Enter due date (optional): ")
    tasks.append({"task": task, "done": False, "due": due_date or "No due date"})
    save_tasks(tasks)
    print(Fore.GREEN + "Task added.")

def delete_task(tasks):
    show_tasks(tasks)
    try:
        index = int(input("Enter task number to delete: ")) - 1
        if 0 <= index < len(tasks):
            removed = tasks.pop(index)
            save_tasks(tasks)
            print(Fore.YELLOW + f"Deleted: {removed['task']}")
        else:
            print(Fore.RED + "Invalid number.")
    except ValueError:
        print(Fore.RED + "Please enter a valid number.")

def toggle_task_done(tasks):
    show_tasks(tasks)
    try:
        index = int(input("Enter task number to toggle status: ")) - 1
        if 0 <= index < len(tasks):
            tasks[index]["done"] = not tasks[index]["done"]
            save_tasks(tasks)
            status = "Done" if tasks[index]["done"] else "Not Done"
            print(Fore.CYAN + f"Marked as {status}: {tasks[index]['task']}")
        else:
            print(Fore.RED + "Invalid number.")
    except ValueError:
        print(Fore.RED + "Please enter a valid number.")

def main():
    tasks = load_tasks()
    while True:
        print("\n" + Fore.MAGENTA + "--- To-Do CLI App ---")
        print("1. Show Tasks")
        print("2. Add Task")
        print("3. Delete Task")
        print("4. Toggle Task Done/Not Done")
        print("5. Exit")

        choice = input(Fore.CYAN + "Choose an option (1-5): ")

        if choice == '1':
            show_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            delete_task(tasks)
        elif choice == '4':
            toggle_task_done(tasks)
        elif choice == '5':
            print(Fore.GREEN + "Goodbye! 👋")
            break
        else:
            print(Fore.RED + "Invalid option, try again.")

if __name__ == "__main__":
    main()


"""  Output
--- To-Do CLI App ---
1. Show Tasks
2. Add Task
3. Delete Task
4. Toggle Task Done/Not Done
5. Exit
Choose an option (1-5): 2
Enter task description: learn Python
Enter due date (optional): 30 July
Task added.

--- To-Do CLI App ---
1. Show Tasks
2. Add Task
3. Delete Task
4. Toggle Task Done/Not Done
5. Exit
Choose an option (1-5): 2
Enter task description: assignment 
Enter due date (optional): 22 July
Task added.

--- To-Do CLI App ---
1. Show Tasks
2. Add Task
3. Delete Task
4. Toggle Task Done/Not Done
5. Exit
Choose an option (1-5): 1
1. learn Python [❌] - Due: 30 July
2. assignment  [❌] - Due: 22 July

--- To-Do CLI App ---
1. Show Tasks
2. Add Task
3. Delete Task
4. Toggle Task Done/Not Done
5. Exit
Choose an option (1-5): 4
1. learn Python [❌] - Due: 30 July
2. assignment  [❌] - Due: 22 July
Enter task number to toggle status: 3
Invalid number.

--- To-Do CLI App ---
1. Show Tasks
2. Add Task
3. Delete Task
4. Toggle Task Done/Not Done
5. Exit
Choose an option (1-5): 4
1. learn Python [❌] - Due: 30 July
2. assignment  [❌] - Due: 22 July
Enter task number to toggle status: 2
Marked as Done: assignment 

--- To-Do CLI App ---
1. Show Tasks
2. Add Task
3. Delete Task
4. Toggle Task Done/Not Done
5. Exit
Choose an option (1-5): 3
1. learn Python [❌] - Due: 30 July
2. assignment  [✅] - Due: 22 July
Enter task number to delete: 2
Deleted: assignment 

--- To-Do CLI App ---
1. Show Tasks
2. Add Task
3. Delete Task
4. Toggle Task Done/Not Done
5. Exit
Choose an option (1-5): 1
1. learn Python [❌] - Due: 30 July

--- To-Do CLI App ---
1. Show Tasks
2. Add Task
3. Delete Task
4. Toggle Task Done/Not Done
5. Exit
Choose an option (1-5): 5
Goodbye! 👋
"""
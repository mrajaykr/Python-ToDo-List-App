# todo.py

FILE_NAME = "tasks.txt"


def load_tasks():
    try:
        with open(FILE_NAME, "r") as file:
            return [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        return []


def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        for task in tasks:
            file.write(task + "\n")


def view_tasks(tasks):
    if not tasks:
        print("\nNo tasks found!")
    else:
        print("\n===== TO-DO LIST =====")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")


def add_task(tasks):
    task = input("Enter task: ")
    tasks.append(task)
    save_tasks(tasks)
    print("Task added successfully!")


def remove_task(tasks):
    view_tasks(tasks)

    if tasks:
        try:
            task_num = int(input("Enter task number to remove: "))
            removed = tasks.pop(task_num - 1)
            save_tasks(tasks)
            print(f"Task '{removed}' removed!")
        except (ValueError, IndexError):
            print("Invalid task number!")


tasks = load_tasks()

while True:
    print("\n===== TO-DO LIST MANAGER =====")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        view_tasks(tasks)

    elif choice == "2":
        add_task(tasks)

    elif choice == "3":
        remove_task(tasks)

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice! Please try again.")
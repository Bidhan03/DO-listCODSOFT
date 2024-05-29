class Task:
    def __init__(self, description):
        self.description = description
        self.completed = False

    def mark_complete(self):
        self.completed = True

    def __str__(self):
        status = "Done" if self.completed else "Pending"
        return f"{self.description} [{status}]"


tasks = []


def add_task(description):
    task = Task(description)
    tasks.append(task)
    print(f"Task '{description}' added.")


def list_tasks():
    if not tasks:
        print("No tasks available.")
    else:
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")


def complete_task(index):
    try:
        task = tasks[index - 1]
        task.mark_complete()
        print(f"Task '{task.description}' marked as complete.")
    except IndexError:
        print("Invalid task number.")


def show_menu():
    print("\nTo-Do List Application")
    print("1. Add Task")
    print("2. List Tasks")
    print("3. Complete Task")
    print("4. Exit")


def main():
    while True:
        show_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            description = input("Enter task description: ")
            add_task(description)
        elif choice == "2":
            list_tasks()
        elif choice == "3":
            index = int(input("Enter task number to complete: "))
            complete_task(index)
        elif choice == "4":
            print("Exiting application.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()

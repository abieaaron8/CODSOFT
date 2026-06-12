tasks = []


def view_tasks():
    if not tasks:
        print("\nNo tasks available.")
        return

    print("\n========== TASK LIST ==========")

    for index, task in enumerate(tasks, start=1):
        print(f"{index}. {task['task']} [{task['status']}]")

    completed = sum(1 for task in tasks if task["status"] == "Completed")

    print("\n========== SUMMARY ==========")
    print("Total Tasks:", len(tasks))
    print("Completed:", completed)
    print("Pending:", len(tasks) - completed)


def add_task():
    task_name = input("\nEnter task: ")

    tasks.append({
        "task": task_name,
        "status": "Pending"
    })

    print("Task added successfully.")


def update_task():
    if not tasks:
        print("\nNo tasks available to update.")
        return

    view_tasks()

    try:
        task_no = int(input("\nEnter task number to update: "))

        if 1 <= task_no <= len(tasks):
            new_name = input("Enter updated task name: ")
            tasks[task_no - 1]["task"] = new_name

            print("Task updated successfully.")
        else:
            print("Invalid task number.")

    except ValueError:
        print("Please enter a valid number.")


def mark_completed():
    if not tasks:
        print("\nNo tasks available.")
        return

    view_tasks()

    try:
        task_no = int(input("\nEnter task number to mark as completed: "))

        if 1 <= task_no <= len(tasks):
            tasks[task_no - 1]["status"] = "Completed"

            print("Task marked as completed.")
        else:
            print("Invalid task number.")

    except ValueError:
        print("Please enter a valid number.")


def delete_task():
    if not tasks:
        print("\nNo tasks available to delete.")
        return

    view_tasks()

    try:
        task_no = int(input("\nEnter task number to delete: "))

        if 1 <= task_no <= len(tasks):
            removed = tasks.pop(task_no - 1)

            print(f"Deleted: {removed['task']}")
        else:
            print("Invalid task number.")

    except ValueError:
        print("Please enter a valid number.")


while True:
    print("\n" + "=" * 40)
    print("        TO-DO LIST APPLICATION")
    print("=" * 40)

    print("1. View Tasks")
    print("2. Add Task")
    print("3. Update Task")
    print("4. Mark Task Completed")
    print("5. Delete Task")
    print("6. Exit")

    choice = input("\nEnter your choice (1-6): ")

    if choice == "1":
        view_tasks()

    elif choice == "2":
        add_task()

    elif choice == "3":
        update_task()

    elif choice == "4":
        mark_completed()

    elif choice == "5":
        delete_task()

    elif choice == "6":
        print("\nThank you for using the To-Do List Application.")
        break

    else:
        print("\nInvalid choice. Please select a number between 1 and 6.")

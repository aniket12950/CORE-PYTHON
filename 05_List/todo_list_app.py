# Simple To-Do List Application

tasks = []

while True:
    print("\n--- TO-DO LIST ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        task = input("Enter task: ")
        tasks.append(task)
        print("Task added successfully.")

    elif choice == "2":
        print("\nYour Tasks:")
        if not tasks:
            print("No tasks available.")
        else:
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")

    elif choice == "3":
        num = int(input("Enter task number to remove: "))
        if 1 <= num <= len(tasks):
            removed = tasks.pop(num - 1)
            print("Removed task:", removed)
        else:
            print("Invalid task number.")

    elif choice == "4":
        print("Exiting To-Do List.")
        break

    else:
        print("Invalid choice.")

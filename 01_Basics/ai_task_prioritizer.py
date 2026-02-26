"""
Project: AI-Based Task Prioritizer
Description: Assigns priority to tasks based on keywords using basic NLP
"""

def calculate_priority(task):
    task = task.lower()
    priority = 0

    # Define keyword weights
    keywords = {
        "urgent": 5,
        "important": 4,
        "today": 4,
        "now": 4,
        "meeting": 3,
        "email": 2,
        "buy": 1,
        "call": 2,
        "submit": 3,
        "deadline": 5,
        "tomorrow": 2,
        "later": -1,
        "optional": -2
    }

    for word, score in keywords.items():
        if word in task:
            priority += score

    return priority


def main():
    print("=== AI Task Prioritizer ===")
    task_list = []

    n = int(input("Enter number of tasks: "))
    for i in range(n):
        task = input(f"Task {i+1}: ")
        priority = calculate_priority(task)
        task_list.append((task, priority))

    # Sort tasks by priority (highest first)
    sorted_tasks = sorted(task_list, key=lambda x: x[1], reverse=True)

    print("\n Prioritized Task List:")
    for i, (task, priority) in enumerate(sorted_tasks, 1):
        print(f"{i}. {task}  → Priority Score: {priority}")


if __name__ == "__main__":
    main()

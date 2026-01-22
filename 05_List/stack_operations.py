stack = []

while True:
    print("\n1.Push\n2.Pop\n3.Display\n4.Exit")
    choice = int(input("Enter choice: "))

    if choice == 1:
        item = input("Enter element to push: ")
        stack.append(item)
        print("Pushed:", item)

    elif choice == 2:
        if not stack:
            print("Stack is empty")
        else:
            print("Popped:", stack.pop())

    elif choice == 3:
        print("Stack elements:", stack)

    elif choice == 4:
        break

    else:
        print("Invalid choice")

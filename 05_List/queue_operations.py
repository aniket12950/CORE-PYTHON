queue = []

while True:
    print("\n1.Enqueue\n2.Dequeue\n3.Display\n4.Exit")
    choice = int(input("Enter choice: "))

    if choice == 1:
        item = input("Enter element to enqueue: ")
        queue.append(item)
        print("Enqueued:", item)

    elif choice == 2:
        if not queue:
            print("Queue is empty")
        else:
            print("Dequeued:", queue.pop(0))

    elif choice == 3:
        print("Queue elements:", queue)

    elif choice == 4:
        break

    else:
        print("Invalid choice")

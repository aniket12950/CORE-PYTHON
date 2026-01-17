students = {}   # empty dictionary

while True:
    print("\n----- Student Dictionary Menu -----")
    print("1. Add Student")
    print("2. Update Student")
    print("3. Delete Student")
    print("4. Display All Students")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        name = input("Enter student name: ")
        age = int(input("Enter student age: "))
        marks = int(input("Enter student marks: "))

        students[name] = {"Age": age, "Marks": marks}
        print("Student added successfully!")

    elif choice == 2:
        name = input("Enter student name to update: ")

        if name in students:
            age = int(input("Enter new age: "))
            marks = int(input("Enter new marks: "))

            students[name]["Age"] = age
            students[name]["Marks"] = marks
            print("Student updated successfully!")
        else:
            print("Student not found!")

    elif choice == 3:
        name = input("Enter student name to delete: ")

        if name in students:
            del students[name]
            print("Student deleted successfully!")
        else:
            print("Student not found!")

    elif choice == 4:
        if not students:
            print("No student records available.")
        else:
            print("\nStudent Records:")
            for name, details in students.items():   # for loop used
                print("Name:", name)
                print("Age:", details["Age"])
                print("Marks:", details["Marks"])
                print("-------------------")

    elif choice == 5:
        print("Program exited.")
        break

    else:
        print("Invalid choice! Try again.")

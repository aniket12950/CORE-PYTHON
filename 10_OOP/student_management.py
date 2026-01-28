class Student:
    def __init__(self, roll, name, marks):
        self.roll = roll
        self.name = name
        self.marks = marks

    def display(self):
        print(f"Roll: {self.roll}, Name: {self.name}, Marks: {self.marks}")


class StudentManager:
    def __init__(self):
        self.students = []

    def add_student(self):
        roll = input("Enter Roll No: ")
        name = input("Enter Name: ")
        marks = input("Enter Marks: ")
        self.students.append(Student(roll, name, marks))
        print("Student added successfully.")

    def view_students(self):
        if not self.students:
            print("No students available.")
            return
        print("\n--- Student List ---")
        for student in self.students:
            student.display()

    def search_student(self):
        roll = input("Enter Roll No to search: ")
        for student in self.students:
            if student.roll == roll:
                student.display()
                return
        print("Student not found.")

    def delete_student(self):
        roll = input("Enter Roll No to delete: ")
        for student in self.students:
            if student.roll == roll:
                self.students.remove(student)
                print("Student deleted successfully.")
                return
        print("Student not found.")


manager = StudentManager()

while True:
    print("\n--- Student Management Menu ---")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        manager.add_student()
    elif choice == "2":
        manager.view_students()
    elif choice == "3":
        manager.search_student()
    elif choice == "4":
        manager.delete_student()
    elif choice == "5":
        print("Program exited.")
        break
    else:
        print("Invalid choice.")

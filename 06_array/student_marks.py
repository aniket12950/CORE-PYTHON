class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks  # list of marks

    def calculate_total(self):
        return sum(self.marks)

    def display_details(self):
        print("\nStudent Name:", self.name)
        print("Marks:", self.marks)
        print("Total Marks:", self.calculate_total())


def main():
    students = []

    n = int(input("Enter number of students: "))

    for i in range(n):
        print(f"\nEnter details for Student {i + 1}")
        name = input("Enter name: ")

        marks = []
        subjects = int(input("Enter number of subjects: "))
        for j in range(subjects):
            mark = int(input(f"Enter marks for subject {j + 1}: "))
            marks.append(mark)

        student = Student(name, marks)
        students.append(student)

    print("\n--- Student Marks Details ---")
    for student in students:
        student.display_details()


if __name__ == "__main__":
    main()

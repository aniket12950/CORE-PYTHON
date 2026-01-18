# Base class
class Person:
    def __init__(self, name):
        self.name = name

    def show_name(self):
        print("Name:", self.name)


# Derived class (Level 2)
class Student(Person):
    def __init__(self, name, roll_no):
        super().__init__(name)
        self.roll_no = roll_no

    def show_roll(self):
        print("Roll No:", self.roll_no)


# Derived class (Level 3)
class Result(Student):
    def __init__(self, name, roll_no, marks):
        super().__init__(name, roll_no)
        self.marks = marks

    def show_result(self):
        print("Marks:", self.marks)


# Object creation
obj = Result("Aniket", 101, 85)

# Accessing methods from all levels
obj.show_name()
obj.show_roll()
obj.show_result()

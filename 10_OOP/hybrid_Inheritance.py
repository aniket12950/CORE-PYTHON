# Base class
class Person:
    def display_person(self):
        print("I am a Person")

# Derived class (Single Inheritance)
class Student(Person):
    def display_student(self):
        print("I am a Student")

# Another base class
class Sports:
    def display_sports(self):
        print("I play Sports")

# Derived class (Multiple + Multilevel Inheritance)
class Result(Student, Sports):
    def display_result(self):
        print("I have a Result")

# Creating object of Result class
obj = Result()

# Calling methods
obj.display_person()
obj.display_student()
obj.display_sports()
obj.display_result()

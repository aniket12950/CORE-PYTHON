# Parent class 1
class Father:
    def father_name(self):
        print("Father name is Ram")

# Parent class 2
class Mother:
    def mother_name(self):
        print("Mother name is Sita")

# Child class inheriting from both Father and Mother
class Child(Father, Mother):
    def child_name(self):
        print("Child name is Ravi")

# Object of Child class
c = Child()

# Calling methods
c.father_name()
c.mother_name()
c.child_name()

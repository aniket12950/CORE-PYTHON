class Parent:
    def show_parent(self):
        print("This is the Parent class")

class Child(Parent):   # Child inherits Parent
    def show_child(self):
        print("This is the Child class")

# create object of Child
c = Child()

c.show_child()     # child class method
c.show_parent()    # parent class method (inherited)

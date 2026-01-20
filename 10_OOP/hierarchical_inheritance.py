# Parent class
class Animal:
    def eat(self):
        print("Animal eats food")

# Child class 1
class Dog(Animal):
    def bark(self):
        print("Dog barks")

# Child class 2
class Cat(Animal):
    def meow(self):
        print("Cat meows")

# Creating objects
dog = Dog()
cat = Cat()

# Calling methods
dog.eat()     # From parent class
dog.bark()    # From Dog class

cat.eat()     # From parent class
cat.meow()    # From Cat class

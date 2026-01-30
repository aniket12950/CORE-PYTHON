# Calculator using math library

import math

print("1. Square Root")
print("2. Power")
print("3. Factorial")

choice = int(input("Enter choice: "))

if choice == 1:
    num = int(input("Enter number: "))
    print("Square Root:", math.sqrt(num))

elif choice == 2:
    base = int(input("Enter base: "))
    power = int(input("Enter power: "))
    print("Result:", math.pow(base, power))

elif choice == 3:
    num = int(input("Enter number: "))
    print("Factorial:", math.factorial(num))

else:
    print("Invalid choice")

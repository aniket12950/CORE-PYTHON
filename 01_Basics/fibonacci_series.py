def fibonacci(n):
    a=0
    b=1
    for i in range(n):
        print(a, end=" ")
        temp = a + b 
        a = b 
        b = temp
n = int(input("Enter number of terms:: "))
fibonacci(n)

# Fibonacci Series using WHILE loop
n = int(input("Enter number of terms (while loop): "))

a = 0
b = 1
i = 0

print("Fibonacci Series (While Loop):")
while i < n:
    print(a, end=" ")
    temp = a + b
    a = b
    b = temp
    i += 1

print("\n")

# Fibonacci Series using FOR loop

n = int(input("Enter number of terms (for loop): "))

a = 0
b = 1

print("Fibonacci Series (For Loop):")
for i in range(n):
    print(a, end=" ")
    temp = a + b
    a = b
    b = temp

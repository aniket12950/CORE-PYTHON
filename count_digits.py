# Program to count number of digits in a number

n = int(input("Enter a number: "))
count = 0

if n == 0:
    count = 1
else:
    while n > 0:
        count += 1
        n = n // 10

print("Number of digits:", count)

# File Name: second_largest_number.py

n = int(input("How many numbers? "))

numbers = []
for i in range(n):
    num = int(input("Enter number: "))
    numbers.append(num)

largest = numbers[0]
second_largest = numbers[0]

for i in range(1, n):
    if numbers[i] > largest:
        second_largest = largest
        largest = numbers[i]
    elif numbers[i] > second_largest and numbers[i] != largest:
        second_largest = numbers[i]

print("Second largest number is:", second_largest)

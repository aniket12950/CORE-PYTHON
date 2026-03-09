# Digital Root Program in Python

num = int(input("Enter number: "))
while num >= 10:
    sum_digits = 0

    while num > 0:
        sum_digits += num % 10
        num //= 10   # Integer division

    num = sum_digits

print("Digital Root =", num)

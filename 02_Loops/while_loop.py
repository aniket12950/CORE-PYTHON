num = int(input("Enter a positive number: "))
while num <= 0:
    print("Please enter a positive number.")
    num = int(input("Enter a positive number: "))

print("Valid number received:", num)
print("----------------------")

# Now check even numbers until an odd number is entered
while num % 2 == 0:
    print("You entered an even number:", num)
    num = int(input("Enter another number: "))

    if num % 2 != 0:
        print("You entered an odd number, exiting loop…")
        break

print("----------------------")
print("Final number you entered (odd):", num)

# Palindrome Check for String
text = input("Enter a string: ")
original_text = text
reversed_text = text[::-1]

print("Reversed String:", reversed_text)

if original_text == reversed_text:
    print("The string is a palindrome.")
else:
    print("The string is NOT a palindrome.")

# Palindrome Check for Number
num = int(input("\nEnter a number: "))
original_num = num
reverse_num = 0

while num != 0:
    digit = num % 10
    reverse_num = reverse_num * 10 + digit
    num //= 10

print("Reversed Number:", reverse_num)

if original_num == reverse_num:
    print("The number is a palindrome.")
else:
    print("The number is NOT a palindrome.")


text = input("Enter a string: ")
rev = ""

for ch in text:
    rev = ch + rev

if text == rev:
    print("Palindrome string")
else:
    print("Not a palindrome string")

print("1. INR to USD")
print("2. INR to EUR")
print("3. USD to INR")

choice = int(input("Choose option: "))
amount = float(input("Enter amount: "))

result = 0

if choice == 1:
    result = amount * 0.012
elif choice == 2:
    result = amount * 0.011
elif choice == 3:
    result = amount * 83
else:
    print("Invalid choice")
    exit()

print("Converted Amount =", result)

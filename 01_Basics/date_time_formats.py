# Program to display current date and time in different formats

from datetime import datetime

now = datetime.now()

print("Current Date and Time Formats\n")

print("1. Default format:")
print(now)

print("\n2. Date (DD-MM-YYYY):")
print(now.strftime("%d-%m-%Y"))

print("\n3. Date (YYYY-MM-DD):")
print(now.strftime("%Y-%m-%d"))

print("\n4. Time (HH:MM:SS):")
print(now.strftime("%H:%M:%S"))

print("\n5. Time (12-hour format):")
print(now.strftime("%I:%M:%S %p"))

print("\n6. Full Date:")
print(now.strftime("%A, %d %B %Y"))

print("\n7. Full Date & Time:")
print(now.strftime("%A, %d %B %Y %I:%M:%S %p"))

print("\n8. Short Date:")
print(now.strftime("%d/%m/%y"))

print("\n9. Month Name:")
print(now.strftime("%B"))

print("\n10. Day Name:")
print(now.strftime("%A"))

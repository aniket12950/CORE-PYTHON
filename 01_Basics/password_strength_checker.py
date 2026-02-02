#importing regex module which will help in pattern matching

import re 
def check_password_strength(password):
    if len(password) < 8:
        return "Weak Password: Must be at least 8 characters long"

    if not re.search(r"[A-Z]", password):
        return "Weak Password: Add at least one uppercase letter"

    if not re.search(r"[a-z]", password):
        return "Weak Password: Add at least one lowercase letter"

    if not re.search(r"[0-9]", password):
        return "Weak Password: Add at least one digit"

    if not re.search(r"[@$!%*?&]", password):
        return "Weak Password: Add at least one special character"

    return "Strong Password ✅"


# Input from user
password = input("Enter your password: ")
result = check_password_strength(password)
print(result)

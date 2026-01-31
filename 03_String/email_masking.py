email = input("Enter email id: ")

username, domain = email.split("@")

masked_username = username[:3] + "*" * (len(username) - 3)

masked_email = masked_username + "@" + domain

print("Masked Email:", masked_email)

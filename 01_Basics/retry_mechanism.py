attempt=3
while attempt > 0:
    pin=input("Enter the PIN code: ")
    if pin =="1234":
        print("Access granted.")
        break
    else:
        attempt-=1
        print(f"Incorrect PIN You have {attempt} attempts left.")
else:
    print("Access Denied Account Locked")
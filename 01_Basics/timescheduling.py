import time

scheduled_time = "15:30"   # HH:MM format

while True:
    current_time = time.strftime("%H:%M")
    
    if current_time == scheduled_time:
        print("Task executed at", current_time)
        break

    time.sleep(30)  # check every 30 seconds

import time

MAX_REQUESTS = 5
TIME_WINDOW = 10  # seconds

request_times = []

def allow_request():
    current_time = time.time()

    # Remove old requests
    while request_times and current_time - request_times[0] > TIME_WINDOW:
        request_times.pop(0)

    if len(request_times) < MAX_REQUESTS:
        request_times.append(current_time)
        return True
    return False


for i in range(10):
    if allow_request():
        print(f"Request {i+1}: Allowed")
    else:
        print(f"Request {i+1}: Blocked (Rate limit exceeded)")
    time.sleep(1)

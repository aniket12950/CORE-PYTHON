import time

def calculate_time(func):
    def wrapper():
        start = time.time()
        func()
        end = time.time()
        print(f"Execution Time: {end - start:.4f} seconds")
    return wrapper

@calculate_time
def sample_task():
    total = 0
    for i in range(1, 1000000):
        total += i
    print("Task completed")

sample_task()

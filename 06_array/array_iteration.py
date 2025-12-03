import numpy as np
# Creating a NumPy array
arr = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90])
print("Array elements:", arr)   
# Iterating through the array using a for loop
for i in arr:
    print("Element:", i)
# Iterating through the array using indices
for index in range(len(arr)):
    print(f"Element at index {index}:", arr[index])
# Using numpy's nditer for iteratioN
for x in np.nditer(arr):
    print("Element using nditer:", x)
    
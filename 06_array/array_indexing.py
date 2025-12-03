import numpy as np
# Creating a NumPy array
arr = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90])
print("Array elements:", arr)
# Accessing elements using indexing
print("First element of array:", arr[0])
print("Last element of array:", arr[-1])
print("Element at index 4:", arr[4])
# Slicing the array
print("Slice from index 2 to 5:", arr[2:6])
print("Slice from index 5 to end:", arr[5:])
print("Slice from start to index 5:", arr[:6])
print("Slice with step 2 from index 0 to 10:", arr[0:10:2]) # arr[start:end:step]
print("Reversed array using slicing:", arr[::-1])
# Two-dimensional array
arr2D = np.array([[11, 12, 13, 14],
                  [21, 22, 23, 24],
                  [31, 32, 33, 34],
                  [41, 42, 43, 44]])
print("Two-dimensional array:\n", arr2D)
# Accessing elements in two-dimensional array
print("Element at row 1, column 2:", arr2D[1, 2])
print("Second row:", arr2D[1, :])
print("Third column:", arr2D[:, 2])
print("Sub-array from row 1 to 3 and column 1 to 3:\n", arr2D[1:4, 1:4])
print("Reversed two-dimensional array:\n", arr2D[::-1, ::-1])
print("Every second row and column:\n", arr2D[::2, ::2])

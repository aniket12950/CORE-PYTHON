import numpy as np
import array as arr

# NumPy array
arr2 = np.array([1,3,4,5,6,9,-1,-3])
print(type(arr2))
print("Array elements:", arr2)

# array module array (unsigned int)
arr1 = arr.array('I', [1,3,4,5,6,9])
print(type(arr1))
# Two-dimensional array using NumPy
arr2D = np.array([[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]])

print("Two-dimensional array:\n", arr2D)

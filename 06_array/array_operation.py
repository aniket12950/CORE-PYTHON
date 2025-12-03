import numpy as np
# Creating a NumPy array
arr = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90])
print("Array elements:", arr)   
# deleting an element
arr_deleted = np.delete(arr, 4) 
print(arr_deleted)
# inserting an element
arr_inserted = np.insert(arr, 4, 55)
print(arr_inserted)
# appending an element
arr_appended = np.append(arr, 100)
print(arr_appended)
# modifying an element
arr_modified = arr.copy()
arr_modified[2] = 35
print(arr_modified)
# resizing the array
arr_resized = np.resize(arr, (3, 3))
print(arr_resized)
# concatenating two arrays
arr2 = np.array([100, 200, 300])
arr_concatenated = np.concatenate((arr, arr2))
print(arr_concatenated)

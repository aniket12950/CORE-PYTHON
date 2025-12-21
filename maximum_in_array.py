import numpy as np
arr = np.array([1, 4, 7, 8])
max_val = arr[0]          # assume first element is max
for i in arr:
    if i > max_val:
        max_val = i
print("Maximum value:", max_val)

min_val=arr[0]
for j in arr:
    if j < min_val:
        min_val = j
print("minimum value",min_val)
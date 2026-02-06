arr = [1, 2, 3, 4, 5]
k = 2   # rotate by 2 positions
k = k % len(arr)  
rotated_array = arr[-k:] + arr[:-k]
print("Original Array:", arr)
print("Rotated Array:", rotated_array)

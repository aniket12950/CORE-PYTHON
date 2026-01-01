# Bubble Sort
def bubble_sort(arr, n):
    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


# Selection Sort
def selection_sort(arr, n):
    for i in range(n):
        small_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[small_index]:
                small_index = j
        arr[i], arr[small_index] = arr[small_index], arr[i]


# Insertion Sort
def insertion_sort(arr, n):
    for i in range(1, n):
        curr = arr[i]
        prev = i - 1
        while prev >= 0 and arr[prev] > curr:
            arr[prev + 1] = arr[prev]
            prev -= 1
        arr[prev + 1] = curr


# Print Array
def print_array(arr, n):
    for i in range(n):
        print(arr[i], end=" ")
    print()



arr = [1, 4, 5, 6, 3]
n = 5

print("Original Array:")
print_array(arr, n)


# insertion_sort(arr, n)
# selection_sort(arr, n)
bubble_sort(arr, n)

print("Sorted Array:")
print_array(arr, n)

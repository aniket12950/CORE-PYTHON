
def binary_search(arr, key):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == key:
            return mid       
        elif arr[mid] < key:
            low = mid + 1    
        else:
            high = mid - 1    

    return -1               

array = [10, 20, 30, 40, 50, 60, 70]
search_key = int(input("Enter element to search: "))

result = binary_search(array, search_key)

if result != -1:
    print("Element found at index:", result)
else:
    print("Element not found")

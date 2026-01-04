# Quick Sort function
def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)

# Partition function
def partition(arr, low, high):
    pivot = arr[high]     # Last element as pivot
    i = low - 1

    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i] # Swap

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


n = int(input("Enter number of products: "))
prices = []

print("Enter product prices:")
for _ in range(n):
    prices.append(int(input()))

quick_sort(prices, 0, n - 1)

print("Sorted product prices:")
for price in prices:
    print(price, end=" ")

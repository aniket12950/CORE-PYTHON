n = int(input("Enter value of n: "))
arr = []

print("Enter", n-1, "elements:")
for i in range(n - 1):
    arr.append(int(input()))

total = n * (n + 1) // 2
sum_arr = 0

for num in arr:
    sum_arr = sum_arr + num

missing = total - sum_arr
print("Missing number is:", missing)

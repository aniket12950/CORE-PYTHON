numbers = [1, 2, 2, 3, 4, 3, 5, 1]
unique_list = []
seen = set()
for num in numbers:
    if num not in seen:
        unique_list.append(num)
        seen.add(num)

print("Original List:", numbers)
print("After Removing Duplicates:", unique_list)

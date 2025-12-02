list1 =['apple', 'banana', 'cherry', 'date',10, 20, 30, 40]
print(list1)
for item in list1:
    print(item)
    if item == 30:
        list1.insert(6,50)
        break

print("Final list after iteration:", list1)
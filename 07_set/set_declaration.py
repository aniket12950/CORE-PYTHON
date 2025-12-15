set1 = {8, 1, 23, 45, 67}
print(set1)
print(type(set1))
set2 = {"apple", "banana", "cherry"}
print(set2)
print(len(set1))
set1.add("orange")
print(set1)

set1.remove(23)
print(set1)

set1.discard(100)  # safe, no error
print(set1)

set1.pop()         # removes a random element
print(set1)

set1.clear()       # empty the set
print(set1)

A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

print("Union:", A | B) #union
print("Intersection:", A & B)#intersection
print("Difference:", A - B)#difference
print("Symmetric Difference:", A ^ B) #symmetric difference

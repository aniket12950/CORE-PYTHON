list = list(range(1, 11))
print("Original list:", list)
# Adding an element to the end of the list
list.append(12)
print("After appending 12:", list)
# Inserting an element at a specific index
list.insert(0, 89)
print("After inserting 89 at index 0:", list)
print("Index of element 5:", list.index(5))
# Removing an element by value
list.remove(5)
print("After removing 5:", list)
# Removing an element by index
removed_element = list.pop(2)
print("After popping element at index 2 :", list)
print("Popped element:", removed_element)
# Counting occurrences of an element
count_4 = list.count(4)
print("Count of element 4:", count_4)
# Sorting the list in ascending order
list.sort()
print("After sorting in ascending order:", list)
# Sorting the list in descending order
list.sort(reverse=True)
print("After sorting in descending order:", list)
# Reversing the list
list.reverse()
print("After reversing the list:", list)
# Copying the list
list_copy = list.copy()
print("Copied list:", list_copy)
# Clearing all elements from the list
list.clear()
print("After clearing the list:", list)
print("Original copied list remains unchanged:", list_copy)
#len() function to get the number of elements in the copied list
print("Length of copied list:",len(list_copy))

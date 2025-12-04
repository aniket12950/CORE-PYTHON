dict={"name":"John", "age":30, "city":"New York"}
print(dict)
#indexing to access values
print("Name:", dict["name"])
print("Age:", dict["age"])
dict1 = {"name":["aniket","rohit","khushal"], "age":[23,24,25], "city":["pune","mumbai","delhi"]}
print(dict1)
print("First person's name:", dict1["name"][0])
print("Second person's city:", dict1["city"][1])
print("Third person's age:", dict1["age"][2])
# Modifying values
dict["age"] = 31
print("Updated Age:", dict["age"])
dict1["city"][2] = "bangalore"
print("Updated Third person's city:", dict1["city"][2])
# Adding new key-value pairs
dict["country"] = "USA"
print("Country:", dict["country"])
dict1["profession"] = ["engineer", "doctor", "artist"]
print("Professions:", dict1["profession"])
# Deleting key-value pairs
del dict["city"]
print("After deletion, dict:", dict)
del dict1["age"]
print("After deletion, dict1:", dict1)
# Using get() method
print("Using get() - Name:", dict.get("name"))
print("Using get() - Age:", dict.get("age", "Not Found"))
# Using keys() and values() methods
print("Keys in dict:", dict.keys())
print("Values in dict:", dict.values())
print("Keys in dict1:", dict1.keys())
print("Values in dict1:", dict1.values())
# Using items() method
print("Items in dict:", dict.items())
print("Items in dict1:", dict1.items())
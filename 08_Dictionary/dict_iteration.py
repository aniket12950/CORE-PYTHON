dict={"name":"John", "age":30, "city":"New York"}
print(dict)
for key in dict:
    print(f"Key: {key}, Value: {dict[key]}")
dict1 = {"name":["aniket","rohit","khushal"], "age":[23,24,25], "city":["pune","mumbai","delhi"]}
print(dict1)
for key, value in dict1.items():
    print(f"Key: {key}, Value: {value}")


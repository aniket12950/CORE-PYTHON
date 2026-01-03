

# Open the file in read mode
file = open("/CORE-PYTHON/11_File_Handling/student.txt", "r")

# Read the content of the file
data = file.read()

# Display the content
print("Contents of the file are:\n")
print(data)

# Close the file
file.close()

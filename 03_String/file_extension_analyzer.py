import string

filename=input("Enter a file name ")
if "." in filename:
    name,extention=filename.rsplit(".",1)#rsplit is used to split from right side and 1 is used to split only once 
    print("File name is:",name)
    print("File extention is:",extention)
else:
    print("Invalid file name")
    
str="aniket Pawar"
print("original string:",str)
print("string repeated 8 times:",str*8)#repeats the string 8 times
print("string in uppercase:",str.upper())#converts string to uppercase
print("sting in lowercase:",str.lower())#converts string to lowercase
print("string with first character capitalized:",str.capitalize())#
print("string with each word capitalized:",str.title())#first letter of each word is capitalized
print("string with swapped case:",str.swapcase())#swaps lowercase to uppercase and vice-versa
print("string length:",len(str))#returns length of string
print("fing a substring 'Pawar' in string:",str.find(('Pawar')))#finds the index of first occurrence of substring
print("replace 'aniket' with 'Khushal':",str.replace('aniket','Khushal'))#replaces old substring with new substring
print("print couting of 'a' in string:",str.count('a'))#counts the number of a in string
print("string after splitting into list:",str.split())#converts string into list of words
print("check if string starts with ' aniket':",str.startswith('aniket')) #useto check if string starts with specified substring  
print("check if string ends with 'Pawar':",str.endswith('Pawar'))#use to check if string ends with specified substring
print("check if all characters are alphanumeric:",str.isalnum())#alphanumeric means alphabetic characters and numbers e.g. a-z, A-Z, 0-9
print("check if all characters are alphabetic:",str.isalpha())#alphabetic means only letters e.g. a-z, A-Z
print("check if all characters are digits:",str.isdigit())#digits means only numbers e.g. 0-9
print("check if all characters are lowercase:",str.islower())#lowercase means only lowercase letters e.g. a-z
print("check if all characters are uppercase:",str.isupper())#uppercase means only uppercase letters e.g. A-Z
print("check if string is whitespace:",str.isspace())#whitespace means spaces, tabs, newlines etc.
print("find index of substring 'Pawar' in string:",str.index('Pawar'))#if substring not found it raises an error


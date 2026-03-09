# Roman to Integer Program in Python

roman_map = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}

roman = input("Enter Roman numeral: ").upper()

result = 0

for i in range(len(roman)):
    value = roman_map[roman[i]]

    if i + 1 < len(roman) and value < roman_map[roman[i + 1]]:
        result -= value
    else:
        result += value

print("Integer value =", result)

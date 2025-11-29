a = 10
b = 5

print("Arithmetic Operators")
print(a + b)   # addition
print(a - b)   # subtraction
print(a * b)   # multiplication
print(a / b)   # division
print(a % b)   # modulus
print(a ** b)  # exponent
print(a // b)  # floor division

print("Comparison Operators")
print(a == b)  # equal to
print(a != b)  # not equal to
print(a > b)   # greater than
print(a < b)   # less than
print(a >= b)  # greater or equal
print(a <= b)  # less or equal

print("Logical Operators")
print(a > 5 and b < 10)  # AND
print(a > 5 or b > 10)   # OR
print(not(a > b))        # NOT

print("Bitwise Operators")
print(a & b)   # bitwise AND
print(a | b)   # bitwise OR
print(a ^ b)   # bitwise XOR
print(~a)      # bitwise NOT
print(a << 1)  # left shift
print(a >> 1)  # right shift

print("Assignment Operators")
x = a          # simple assignment
x += b         # add and assign
x -= b         # subtract and assign
x *= b         # multiply and assign
x /= b         # divide and assign
x %= b         # modulus and assign
x **= 2        # exponent and assign
x //= b        # floor divide and assign

print("Membership Operators")
print(10 in [a, b])      # in
print(20 not in [a, b])  # not in

print("Identity Operators")
print(a is b)       # is
print(a is not b)   # is not

# Armstrong Number Program using while loop 

num = int(input("Enter a number: "))
orig = num
l=len(str(num))
sum = 0     # holds the sum of cubes

while num > 0:
    rem = num % 10
    sum += rem ** l
    num //= 10

if sum == orig:
    print(orig, "is an Armstrong number")
else:
    print(orig, "is NOT an Armstrong number")

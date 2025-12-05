#define a add function that takes two parameters and returns their sum
def add(a,b):
    return a+b
a=add(5,8)
print(" sum is",a)
#define a function to find the maximum of two numbers
def maximum(x,y):
    if x>y:
        return x
    else:
        return y
m=maximum(10,20)
print("maximum is",m)
#define a function to check if a number is even or odd
def is_even(n):
    if n%2==0:
        return True
    else:
        return False
num=7
result=is_even(num)
if result:
    print(num,"is even")
else:
    print(num,"is odd")
#define a function to calculate factorial of a number
def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)
fact=factorial(5)
print("factorial is",fact)
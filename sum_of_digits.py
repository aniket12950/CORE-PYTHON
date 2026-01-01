num=int(input("Enter a number: "))
def sum_of_digits(n):
    total=0
    while n>0:
        digit=n%10
        total+=digit
        n=n//10
    return total    
result=sum_of_digits(num)
print("Sum of digits:",result)
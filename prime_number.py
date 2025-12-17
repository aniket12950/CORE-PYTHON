num=int(input("enter a number"))
if num<=1:
    print("Not prime number")
else:
    for i in range(2,num):
        if i%num==0:
            print("Not prime number")
            break
    else:
        print("prime number")
            
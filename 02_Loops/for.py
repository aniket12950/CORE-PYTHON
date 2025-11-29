a=int(input("enter a number:\n"))
print("----------------")
for i in range(1,11):
    print(a*i,"\n")
print("----------------")
#use a step argument    
for i in range(1,11,2):
    print(a*i,"\n")  
print("----------------")
#nested for loop
b=10
c=6
for i in range(1,b+1):              
    for j in range(2,c+5):
        print(i*j,"\t",end="")
    print("\n")
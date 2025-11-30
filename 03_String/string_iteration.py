str="anikert pawar patil"
str = str.replace(" ","") #removeing middle space 
i=0             
print(str)
for char in str:
    print(i,"=",char)
    i+=1
#print using index
for index in range(len(str)):
    print(index,"=",str[index])
   
   
    

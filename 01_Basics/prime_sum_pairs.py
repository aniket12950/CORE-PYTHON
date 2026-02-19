def primeadd(num):
    arr=[2]
    for i in range(1,35):  
        for j in range(2,i):
            if i%j==0:
                break; 
            else:
                arr.append(i)
                break;

    
    for k in arr:
        
        for m in arr:
            if m+k==num:
                print(m,"+",k,"=",num)
  
primeadd(34)
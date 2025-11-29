for i in range(10):
    if i==5:
        print("Loop is broken at i =",i)
        break
    print("i =",i)
print("Loop ended.")  
# use continue statement
for j in range(10):
    if j==5:
        print("Skipping the iteration at j =",j)
        continue
    print("j =",j)
                                           
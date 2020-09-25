
n=int(input("Enter number: "))

for i in range(n,-1,-1):
    for j in range(n-i,0,-1):
     print(" ",end=" ")
    for k in range(i,-1,-1):
        print(k,end=" ")
    for k in range(1,i%(n+1)+1):
        print(k,end=" ")
    print("\n")



for i in range(1,(n+1)):
    for j in range(0,n-i):
        print(" ",end=" ")
    for k in range(i,-1,-1):
        print(k,end=" ")
    for k in range(1,i+1):
        print(k,end=" ")
    print("\n")
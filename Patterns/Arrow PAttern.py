n=int(input())
n1=(n+1)//2
n2=n-n1
i=1
while i<=n1:
    q=1
    while q<=i-1:
        print(" ",end="")
        q+=1
    j=1
    while j<=i:
        print("* ",end="")
        j+=1
    print()
    i+=1
i=1
while i<=n2:
    q=1
    while q<=n2-i:
        print(" ",end="")
        q+=1
    j=1
    while j<=n2-i+1:
        print("* ",end="")
        j+=1
    print()
    i+=1
## Creating A Pattern For Beginner to learn the complexicity they could get
n=int(input())
n1=(n+1)//2  ## n1 will be used to create a pattern above half
n2=n-n1      ## n2 will be used to create below half pattern
i=1
while i<=n1:
    q=1
    while q<=i-1:     ## While is usebecause it will break the loop when condition will become false
        print(" ",end="")
        q+=1
    j=1
    while j<=i:
        print("* ",end="")
        j+=1
    print()
    i+=1  ## i is incremented at last of loop cause to meet the condtion given at first
i=1    ## value is assigned again for the second half pattern
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
    i+=1   ## i is incremented at last of loop cause to meet the condtion given at first
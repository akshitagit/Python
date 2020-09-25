n=int(input("Enter N: "))
for i in range(n,-1,-1):
    s = (
            " ".join(map(str,range(i,-1,-1))) 
            + " "
            + " ".join(map(str,range(1,i+1)))
        ).strip()
    s = s.strip()
    print(s.center(n*4+1))
for i in range(1,n+1):
    s = (
            " ".join( map( str , range(i,-1,-1) ) )
            + " "
            + " ".join(map(str,range(1,i+1)))
        ).strip()
    print(s.center(n*4+1))
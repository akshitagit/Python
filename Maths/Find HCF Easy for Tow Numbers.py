def calcu(x,y):
    if x>y:
        smaller=y
    else:
        smaller=x
    i=1
    while i<=smaller:
        if ((x%i==0) and (y%i==0)):
            hcf=i
        i+=1
    print(hcf)
x=int(input("Enter Your First Number:"))
y=int(input("Enter your Second Number:"))
calcu(x,y)
#Fibonacci Series

n = int(input("Enter a Number: "))
n1 = 0
n2 = 1
count = 0

if n == 0:
    print("Enter a positive Number!")
elif n == 1:
    print(n1)
else:
   print("Fibonacci Series:")
   while count < n:
       print(n1)
       nth = n1 + n2
       # new values
       n1 = n2
       n2 = nth
       count += 1
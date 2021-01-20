n = int(input())
a = int(input())
b = int(input())

for i in range(1,n+1):
    print('Fizz'*(i%a<1) +'Buzz'*(i%b<1) or i)

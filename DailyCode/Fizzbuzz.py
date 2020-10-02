n = int(input("Enter n: "))
a = int(input("Enter a: "))
b = int(input("Enter b: "))
for(i in range(1, n+1)):
    if(i % a == 0 && i % b == 0):
        print("FizzBuzz")
    elif(i%a == 0):
        print("Fizz")
    elif(i%b == 0):
        print("Buzz")
    else:
        print(i)

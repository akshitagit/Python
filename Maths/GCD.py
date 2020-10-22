def gcd(a, b):
    if(b == 0):
        return a
    return gcd(b, a%b)

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print(f"GCD of number {a} and {b} is {GCD(a,b)}")

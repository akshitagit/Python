def isPrime(n) : 
    # Corner cases 
    if (n <= 1) : 
        return False
    if (n <= 3) : 
        return True
  
    # This is checked so that we can skip  
    # middle five numbers in below loop 
    if (n % 2 == 0 or n % 3 == 0) : 
        return False
  
    i = 5
    while(i * i <= n) : 
        if (n % i == 0 or n % (i + 2) == 0) : 
            return False
        i = i + 6
  
    return True

n = int(input('Enter the number : '))
arr = []
for j in range(0,n+1) :
    if isPrime(j) :
        arr.append(j)
if len(arr) > 0 :
    for j in arr :
        print(j)
else :
    print('No prime numbers')






def calcGCD(a,b):
    return b if a%b==0 else calcGCD(b, a%b)

if __name__ == '__main__':
    
    n = int(input())
    arr = list(map(int, input().split()))
    gcd = calcGCD(arr[0], arr[1])
    
    for i in range(2, len(arr)):
        gcd = calcGCD(gcd, arr[i])
    
    print(gcd)


# function to find hcf of given numbers
def calcHCF(a,b):
    return b if a%b==0 else calcHCF(b, a%b)

if __name__ == '__main__':
    
    n = int(input())
    arr = list(map(int, input().split()))
    hcf = calcHCF(arr[0], arr[1])
    
    for i in range(2, len(arr)):
        hcf = calcHCF(hcf, arr[i])
    
    print(hcf)

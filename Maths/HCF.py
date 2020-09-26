
# function to find hcf of given numbers
def calcHCF(a,b):
    return b if a%b==0 else calcHCF(b, a%b)

# Function for finding fibonacci series upto any number
def fibonacci(n):
    if(n>20):
        return
    result=[]
    a=0
    b=0
    c=1
    while(n>0):
        result.append(a)
        a=b+c
        c=b
        b=a
        n-=1
    

if __name__ == '__main__':
    
    n = int(input())
    arr = list(map(int, input().split()))
    hcf = calcHCF(arr[0], arr[1])
    
    for i in range(2, len(arr)):
        hcf = calcHCF(hcf, arr[i])
    
    print(hcf)

    

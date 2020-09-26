def fibonacci(memo, n):
    if(n <= 2):
        return 1
    if(n in memo):
        return memo[n]

    memo[n] = fibonacci(memo, n-1) + fibonacci(memo, n-2)
    return memo[n]

n = int(input())
memo = {}
print(fibonacci(memo, n))

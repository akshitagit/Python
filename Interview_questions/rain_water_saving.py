n = int(input())
elevation = list(map(int, input().split()))

maxFromLeft = [0 for i in range(n)]
maxFromRight = [0 for i in range(n)]

maxFromLeft[0] = elevation[0]
for i in range(1, n):
    maxFromLeft[i] = max(maxFromLeft[i-1], elevation[i])

maxFromRight[n-1] = elevation[n-1]
for i in range(n-2, -1, -1):
    maxFromRight[i] = max(maxFromRight[i+1], elevation[i])

ans = 0
for i in range(n):
    ans += min(maxFromLeft[i], maxFromRight[i]) - elevation[i]

print(ans)
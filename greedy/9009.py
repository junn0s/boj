dp = [0] * 45
dp[0] = 1
dp[1] = 1

for i in range(2, 45):
    dp[i] = dp[i-1] + dp[i-2]
    
t = int(input())
for _ in range(t):
    n = int(input())
    arr = []
    for i in range(44, -1, -1):
        if n > 0 and n >= dp[i]:
            arr.append(dp[i])
            n -= dp[i]
    arr.sort()
    print(*arr)
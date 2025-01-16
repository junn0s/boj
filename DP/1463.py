def makeOne(n):
    dp = [0] * (n+10)
    dp[0] = 0; dp[1] = 0; dp[2] = 1; dp[3] = 1
    for i in range(4, n+1):
        dp[i] = dp[i-1] + 1
        if i % 6 == 0:
            dp[i] = min(dp[int(i/2)] + 1, dp[int(i/3)] + 1, dp[i])
        elif i % 3 == 0:
            dp[i] = min(dp[int(i/3)] + 1, dp[i])
        elif i % 2 == 0:
            dp[i] = min(dp[int(i/2)] + 1, dp[i])
            
    return dp[n]



n = int(input())
print(makeOne(n))


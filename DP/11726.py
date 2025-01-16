def tile(n):
    dp = [0] * (n+10)
    dp[0] = 0; dp[1] = 1; dp[2] = 2
    for i in range(3, n+1):
        dp[i] = dp[i-1] + dp[i-2]
        dp[i] %= 10007
    
    return dp[n]

n = int(input())
print(tile(n))
def t(n):
    dp = [0] * (n+1)
    dp[0] = 1
    
    for i in range(1, n+1):
        temp = 0
        for j in range(0, i):
            temp += (dp[j] * dp[i-j-1])
        dp[i] = temp
    
    return dp[n]

n = int(input())
print(t(n))
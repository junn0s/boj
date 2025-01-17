def stone(n):
    dp = ['none'] * (n+10)
    dp[1] = 'CY'; dp[2] = 'SK'; dp[3] = 'CY'
    
    for i in range(4, n+1):
        if dp[i-1] == 'CY' and dp[i-3] == 'CY':
            dp[i] = 'SK'
        else:
            dp[i] = 'CY'
            
    return dp[n]


n = int(input())
print(stone(n))



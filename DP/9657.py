def stone(n):
    dp = ['none'] * (n+10)
    dp[1] = 'SK'; dp[2] = 'CY'; dp[3] = 'SK'; dp[4] = 'SK'
    
    for i in range(5, n+1):
        if dp[i-1] == 'SK' and dp[i-3] == 'SK' and dp[i-4] == 'SK':
            dp[i] = 'CY'
        else:
            dp[i] = 'SK'
            
    return dp[n]


n = int(input())
print(stone(n))
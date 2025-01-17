def stone(n):
    dp = ['none'] * (n+10)
    dp[1] = 'CY'; dp[2] = 'SK'; dp[3] = 'CY'; dp[4] = 'SK'
    
    for i in range(5, n+1):
        if dp[i-1] == 'SK' and dp[i-3] == 'SK' and dp[i-4] == 'SK':
            dp[i] = 'CY'
        else:
            dp[i] = 'SK'
            
    return dp[n]


n = int(input())
print(stone(n))



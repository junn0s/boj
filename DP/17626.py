import math
n = int(input())

def foursquares(n):
    INF = float('inf')
    dp = [INF] * (n+1)
    dp[0] = 0
    #res = 0
    
    #if n > 100:
    #    while n > 100:
    #        sqrt_n = math.floor(math.sqrt(n))
    #        n -= sqrt_n ** 2
    #        res += 1
    
    for i in range(1, n+1):
        j = 1
        while j * j <= i:
            dp[i] = min(dp[i], dp[i - j * j] + 1)
            j += 1
            
    return dp[n] #+ res


print(foursquares(n))
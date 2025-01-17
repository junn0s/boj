k = int(input())

def fibo(k):
    if k < 0:
        return 0
    
    dp = [0] * (k+3)
    dp[0] = 1; dp[1] = 1
    
    for i in range(2, k+1):
        dp[i] = dp[i-1] + dp[i-2]
        
    return dp[k]

print(fibo(k-2), fibo(k-1))

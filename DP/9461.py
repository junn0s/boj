def P(N):
    dp = [0] * (N+5)
    dp[0] = 1; dp[1] = 1; dp[2] = 1; dp[3] = 2; dp[4] = 2
    for i in range(5, N+1):
        dp[i] = dp[i-1] + dp[i-5]
    
    return dp[N]



T = int(input())
for _ in range(T):
    N = int(input())
    print(P(N-1))
    
    

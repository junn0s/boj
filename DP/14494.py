#1 1 1  1  1  1
#1 3 5  7  9  11
#1 5 13 25 41 61
#1 7 25 63 129
#1 9 





def maze(n, m):
    dp = [[0 for _ in range(m)] for _ in range(n)]
    dp[0][0] = 1
    for i in range(m):
        dp[0][i] = 1
    for j in range(n):
        dp[j][0] = 1
       
    for i in range(1, n):
        for j in range(1, m):    
            dp[i][j] = (dp[i-1][j] + dp[i][j-1] + dp[i-1][j-1]) % 1000000007
            
    return dp[n-1][m-1]


n,m = map(int, input().split())
print(maze(n,m))
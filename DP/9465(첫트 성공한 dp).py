import sys
input = sys.stdin.readline

def sticker(arr:list, n):
    dp = arr
    if n == 1:
        return max(dp[0][0], dp[1][0])
    
    dp[0][1] = dp[1][0] + dp[0][1]
    dp[1][1] = dp[0][0] + dp[1][1]
    
    for i in range(2, n):
        dp[0][i] = max(dp[1][i-2] + dp[0][i] , dp[1][i-1] + dp[0][i])
        dp[1][i] = max(dp[0][i-2] + dp[1][i] , dp[0][i-1] + dp[1][i])
    
    return max(dp[0][n-1], dp[1][n-1])
    
    
T = int(input().rstrip())
for _ in range(T):
    n = int(input().rstrip())
    arr = list()
    for _ in range(2):
        temp = list(map(int, input().rstrip().split()))
        arr.append(temp)
    print(sticker(arr, n))
    
    
    
#50 10 100 20 40
#30 50 70  10 60

#50 40  max(130, 200)     140        250
#30 100 max(40+70, 50+70) 210, 50   260,200
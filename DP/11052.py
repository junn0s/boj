import sys
input = sys.stdin.readline

def card(arr:list, n):
    dp = [0] * n
    dp[0] = arr[0]
    
    for i in range(1, n):
        dp[i] = arr[i]
        for j in range(n-1):
            dp[i] = max(dp[i], dp[j] + dp[(i-j-1)]) 
            
    return dp[n-1]


n = int(input())
arr = list(map(int, input().rstrip().split()))
print(card(arr, n))
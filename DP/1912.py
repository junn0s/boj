import sys 
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().rstrip().split()))
dp = [0 for _ in range(n)]

dp[0] = arr[0]
for i in range(1, n):
    dp[i] = max(arr[i], dp[i-1] + arr[i])
    
dp.sort(reverse=True)
print(dp[0])

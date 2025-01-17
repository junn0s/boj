import sys
input = sys.stdin.readline


dp = [0] * (10001)
dp[0] = 1; dp[1] = 1
    
for i in range(2, 10000):
    dp[i] = (dp[i-1] + dp[i-2])




T = int(input())
for i in range(T):
    p, q = map(int, input().rstrip().split())
    res = dp[p-1]
    print("Case #%d:" % (i+1), str(res % q))
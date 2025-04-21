# 1,2,3 더하기 4
# 15989

import sys
input = sys.stdin.readline

dp = [0] * (10000 + 1)
dp[0] = 1
arr = [1, 2, 3]
for i in arr:
    for j in range(i, 10000 + 1):
        dp[j] += dp[j - i]

n = int(input())
for _ in range(n):
    num = int(input())
    print(dp[num])
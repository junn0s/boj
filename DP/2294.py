# 동전 2
# DP

INF = 200000
n, k = map(int, input().split())
dp = [INF for _ in range(k + 1)]
dp[0] = 0
coins = []
for _ in range(n):
    coin = int(input())
    coins.append(coin)

for coin in coins:
    for i in range(coin, k+1):
        dp[i] = min(dp[i], dp[i - coin] + 1)

if dp[k] != INF:
    print(dp[k])
else:
    print(-1)

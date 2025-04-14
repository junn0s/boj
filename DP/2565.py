# 2565 전깃줄

n = int(input())
a = [0] * n
for i in range(n):
    a[i] = list(map(int, input().split()))
a.sort(key=lambda x: x[0])
dp = [1] * n
for i in range(n):  
    for j in range(i):
        if a[i][1] > a[j][1]:
            dp[i] = max(dp[i], dp[j] + 1)
print(n - max(dp))



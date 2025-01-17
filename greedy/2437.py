import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

if n == 1:
    if arr[0] == 1:
        print(2)
    else:
        print(1)
    sys.exit()

arr.sort()
dp = [0] * n
dp[0] = arr[0]

if arr[0] != 1:
    print(1)
    sys.exit()

for i in range(1, n):
    dp[i] = dp[i-1] + arr[i]

res = 0
for i in range(1, n):
    if dp[i-1] + 1 < arr[i]:
        res = dp[i-1] + 1
        break
        
if res != 0:
    print(res)
else:
    print(dp[n-1] + 1)
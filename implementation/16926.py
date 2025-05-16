import sys
input = sys.stdin.readline


n, m, r = map(int, input().split())
arr = []
for _ in range(n):
    tmp = list(map(int, input().split()))
    arr.append(tmp)

minval = min(n, m)
minval = minval // 2
for _ in range(r):
    for k in range(0, minval):
        tmp = arr[k][k]
        for i in range(k, m-1-k):
            arr[k][i] = arr[k][i+1]
        for i in range(k, n-1-k):
            arr[i][m-1-k] = arr[i+1][m-1-k]
        for i in range(m-2-k, -1+k, -1):
            arr[n-1-k][i+1] = arr[n-1-k][i]
        for i in range(n-2-k, -1+k, -1):
            arr[i+1][k] = arr[i][k]
            if i == k:
                arr[i+1][k] = tmp

for i in range(n):
    for j in range(m):
        print(arr[i][j], end=' ')
    print()


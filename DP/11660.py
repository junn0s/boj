import sys
input = sys.stdin.readline

n,m = map(int, input().split())
arr = []
for _ in range(n):
    tmp = list(map(int, input().split()))
    arr.append(tmp)
prefixArr = [[0 for _ in range(n)]for _ in range(n)]
prefixArr[0][0] = arr[0][0]
for i in range(1, n):
    prefixArr[0][i] = prefixArr[0][i-1] + arr[0][i]
    prefixArr[i][0] = prefixArr[i-1][0] + arr[i][0]
for i in range(1, n):
    for j in range(1, n):
        prefixArr[i][j] = prefixArr[i][j-1] + arr[i][j] + prefixArr[i-1][j] - prefixArr[i-1][j-1]

for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    x1 -= 1
    y1 -= 1
    x2 -= 1
    y2 -= 1
    a = prefixArr[x2][y2]
    if y1 == 0:
        b = 0
    else:
        b = prefixArr[x2][y1-1]
    if x1 == 0:
        c = 0
    else:
        c = prefixArr[x1-1][y2]
    if x1 == 0 or y1 == 0:
        d = 0
    else:
        d = prefixArr[x1-1][y1-1]
    res = a - b - c + d
    print(res)
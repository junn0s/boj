# 데칼코마니

n, m = map(int, input().split())
arr = [[0 for _ in range(m)] for _ in range(n)]
for i in range(n):
    info = input()
    for j in range(m):
        arr[i][j] = info[j]

for i in range(n):
    for j in range(m//2):
        if arr[i][j] != '.':
            arr[i][m-j-1] = arr[i][j]

for i in range(n):
    for j in range(m//2, m):
        if arr[i][j] != '.':
            arr[i][m-j-1] = arr[i][j]

for i in range(n):
    for j in range(m):
        print(arr[i][j], end='')
    print()

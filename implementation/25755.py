# 거울반사

w, n = input().split()
n = int(n)
arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))

for i in range(n):
    for j in range(n):
        if arr[i][j] == 2:
            arr[i][j] = 5
        elif arr[i][j] == 5:
            arr[i][j] = 2

if w == 'D' or w == 'U':
    for i in range(n//2):
        arr[i] , arr[n-i-1] = arr[n-i-1], arr[i]
elif w == 'L' or w == 'R':
    for i in range(n):
        for j in range(n//2):
            arr[i][j], arr[i][n-j-1] = arr[i][n-j-1], arr[i][j]

for i in range(n):
    for j in range(n):
        if arr[i][j] in [1,2,5,8]:
            continue
        else:
            arr[i][j] = '?'

for i in range(n):
    for j in range(n):
        print(arr[i][j], end=' ')
    print()
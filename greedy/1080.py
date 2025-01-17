import sys

n, m = map(int, input().split())
arr1 = []
arr2 = []
for _ in range(n):
    tmp = list(input())
    arr1.append(tmp)
for _ in range(n):
    tmp = list(input())
    arr2.append(tmp)
    
if n < 3 or m < 3:
    if arr1 == arr2:
        print(0)
    else:
        print(-1)
    sys.exit()
    
cnt = 0
for i in range(n-2):
    for j in range(m-2):
        if arr1[i][j] != arr2[i][j]:
            cnt += 1
            for k in range(i, i+3):
                for l in range(j, j+3):
                    if arr1[k][l] == '0':
                        arr1[k][l] = '1'
                    else:
                        arr1[k][l] = '0'


if arr1 == arr2:
    print(cnt)
else:
    print(-1)
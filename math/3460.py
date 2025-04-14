# 이진수
T = int(input())
for _ in range(T):
    n = int(input())
    arr = []
    for i in range(19, -1, -1):
        tmp = 2 ** i
        if n // tmp == 1:
            n -= tmp
            arr.append(1)
        else:
            arr.append(0)
    arr.reverse()
    resarr = []
    for i in range(len(arr)):
        if arr[i] == 1:
            resarr.append(i)
    print(*resarr)
import sys

n, score, p = map(int, input().split())
if n == 0:
    print(1)
    sys.exit()

arr = list(map(int, input().split()))

tmp = 0
idx = 0
for i in range(n):
    if score > arr[i]:
        arr.insert(i, score)
        tmp = 1
        idx = i
        break

if tmp == 0:
    arr.append(score)
    idx = n

if idx >= p:
    print(-1)
else:
    for i in range(n+1):
        if arr[i] == score:
            print(i+1)
            break

n, score, p = map(int, input().split())
# 톱니바퀴

import sys
from collections import deque
input = sys.stdin.readline

arr = deque()
for _ in range(4):
    tmp = input().strip()
    tmparr = deque()
    for item in tmp:
        tmparr.append(item)
    arr.append(tmparr)

k = int(input())
for _ in range(k):
    num, r = map(int, input().split())
    num -= 1
    rotate = [0, 0, 0, 0]
    rotate[num] = r

    for i in range(num, 0, -1):
        if arr[i][6] != arr[i-1][2]:
            rotate[i-1] = -rotate[i]
        else:
            break

    for i in range(num, 3):
        if arr[i][2] != arr[i+1][6]:
            rotate[i+1] = -rotate[i]
        else:
            break

    for i in range(4):
        if rotate[i] == 0:
            continue
        if rotate[i] == -1:
            tmp = arr[i].popleft()
            arr[i].append(tmp)
        else:
            tmp = arr[i].pop()
            arr[i].appendleft(tmp)

res = 0
if arr[0][0] == '1':
    res += 1
if arr[1][0] == '1':
    res += 2
if arr[2][0] == '1':
    res += 4
if arr[3][0] == '1':
    res += 8

print(res)

# 6 2 / 6 2 / 6 2 / 6 2
# -1 반시계 1 시계
# 좌회전 : popleft 후 append
# 우회전 : pop 후 appendleft


import sys
input = sys.stdin.readline


n = int(input())
tmp = list(map(int, input().split()))
balloon = dict()
res = []
for i in range(len(tmp)):
    balloon[i+1] = tmp[i]

index = 1
zero_count = 0
for _ in range(n):
    if zero_count == n-1:
        for key, value in balloon.items():
            if value != 0:
                res.append(key)
                break
    res.append(index)
    tmp = balloon[index]
    balloon[index] = 0
    zero_count += 1
    i = 0
    if tmp > 0:
        while i < tmp and zero_count < n-1:
            index += 1
            if index > n:
                index = index % n
            if balloon[index] != 0:
                i += 1

    else:
        tmp = -tmp
        while i < tmp and zero_count < n-1:
            index -= 1
            if index < 1:
                index += n
            if balloon[index] != 0:
                i += 1
                

res.pop()
print(*res)
        




# 효율적인 deque이용한 코드
'''

from collections import deque

n = int(input())
balloons = list(map(int, input().split()))

dq = deque((i+1, balloons[i]) for i in range(n))

result = []

while dq:
    idx, val = dq.popleft()
    result.append(idx)

    if val > 0:
        dq.rotate(-(val-1))
    elif val < 0:
        dq.rotate(-val)

print(*result)

'''
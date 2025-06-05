# 수열

import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())
arr = deque(map(int, input().split()))

prefix_arr = deque()
for i in range(k):
    prefix_arr.append(arr[i])
tmp = sum(prefix_arr)
res = tmp

for i in range(k, n):
    a = prefix_arr.popleft()
    prefix_arr.append(arr[i])
    b = arr[i]
    current = tmp - a + b
    res = max(res, current)
    tmp = current

print(res)
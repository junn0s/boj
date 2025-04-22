# 출제비 재분배

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))
resarr = [0] * (n+m)
for i in range(n):
    tmp = list(map(int, input().split()))
    tmp[i] += arr[i] - sum(tmp)
    for j in range(len(tmp)):
        resarr[j] += tmp[j]

print(*resarr)
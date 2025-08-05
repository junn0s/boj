# 나누기

import sys
input = sys.stdin.readline

n = int(input())
f = int(input())

n = (n // 100) * 100
for i in range(100):
    if (n + i) % f == 0:
        res = n + i
        break

res = str(res)
print(res[-2:])
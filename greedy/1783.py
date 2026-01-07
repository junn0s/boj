# 병든 나이트

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
result = 0

if n >= 3 and m >= 7:
    result = m - 2
elif n == 1 or m == 1:
    result = 1
elif n >= 3 and m >= 2:
    result = min(4, m)
elif n == 2 and m >= 2:
    result = min(4, (m-1)//2 + 1)
print(result)

# 미역은 식물 아닌데요

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [] # 절대로 불가능한 놈들
res_p = [] 
res_m = []

for _ in range(m):
    a, b, c = input().split()
    a = int(a)
    c = int(c)
    if b == 'P' and c == 1:
        res_p.append(a)
    elif b == 'M' and c == 0:
        res_m.append(a)
    elif b == 'P' and c == 0:
        arr.append(a)
    elif b == 'M' and c == 1:
        arr.append(a)

resres = set(res_m) & set(res_p)
min = len(resres)
max = n - len(set(arr))
print(min, max)
# 전구

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
lights = list(map(int, input().split()))
for _ in range(m):
    a, b, c = map(int, input().split())
    if a == 1: lights[b-1] = c
    elif a == 2:
        for i in range(b-1, c):
            if lights[i] == 0: lights[i] = 1
            else: lights[i] = 0
    elif a == 3:
        for i in range(b-1, c):
            lights[i] = 0
    else:
        for i in range(b-1, c):
            lights[i] = 1

print(*lights)
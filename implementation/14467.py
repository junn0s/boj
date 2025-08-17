# 소가 길을 건너간 이유 1

import sys
input = sys.stdin.readline

cows = [None] * 10
n = int(input())
count = 0

for _ in range(n):
    num, loc = map(int, input().split())
    if cows[num-1] is not None and cows[num-1] != loc:
        count += 1
    cows[num-1] = loc

print(count)
    
# 가운데를 말해요

import sys
import heapq
input = sys.stdin.readline

n = int(input())

h = heapq()
for _ in range(n):
    num = int(input())
    heapq.heappush(h, num)

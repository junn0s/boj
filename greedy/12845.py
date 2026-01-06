# 모두의 마블

import sys
input = sys.stdin.readline

n = int(input())
level = list(map(int, input().split()))
level = sorted(level, reverse=True)

print((sum(level) - level[0]) + (level[0] * (n-1)))




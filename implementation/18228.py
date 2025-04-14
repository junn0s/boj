# 펭귄추락대책위원회

import sys
input = sys.stdin.readline

n = int(input())
powarr = list(map(int, input().split()))
index = 0
for i in range(n):
    if powarr[i] == -1:
        index = i
        break

print(min(powarr[:i]) + min(powarr[i+1:]))
# 숫자 카드

import sys
input = sys.stdin.readline

n = int(input())
cards = set(map(int, input().split()))
m = int(input())
check = list(map(int, input().split()))

for i in range(m):
    if check[i] in cards:
        check[i] = 1
    else:
        check[i] = 0

print(*check)


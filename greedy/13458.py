# 시험 감독

import sys
input = sys.stdin.readline

n = int(input())
A = list(map(int, input().split()))
B, C = map(int, input().split())

master = n
slave = 0
for i in range(n):
    if A[i] > B:
        tmp = A[i]-B
        slave += tmp // C
        if tmp % C:
            slave += 1

print(master + slave)
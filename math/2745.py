# 진법 변환

import sys
input = sys.stdin.readline

n, b = input().split()
b = int(b)

print(int(n, b))

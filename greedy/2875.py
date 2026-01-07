# 대회 or 인턴

import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
print(min(n//2, m, (n+m-k)//3))
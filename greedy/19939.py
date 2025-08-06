# 박 터뜨리기

import sys
input = sys.stdin.readline

n, k = map(int, input().split())
t = (k * (k+1)) / 2
if n < t:
    print(-1)
elif (n-t) % k == 0:
    print(k-1)
else:
    print(k)

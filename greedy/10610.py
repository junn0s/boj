# 30

import sys
input = sys.stdin.readline

n = str(input().strip())
n = ''.join(sorted(n, reverse=True))
if '0' in n:
    result = sum(map(int, n))
    if result % 3 != 0:
        print(-1)
    else:
        print(n)
else:
    print(-1)
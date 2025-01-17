import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n = int(input())
    res = 0
    for _ in range(n):
        a, b, c = map(int, input().split())
        tmp = max(a, b, c)
        if tmp > 0:
            res += tmp
    print(res)
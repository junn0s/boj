import math

T = int(input())
for _ in range(T):
    n, m = map(int, input().split())
    comb = math.comb(m, n)
    print(comb)
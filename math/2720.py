# 세탁소 사장 동혁

t = int(input())
for _ in range(t):
    n = int(input())
    q = n // 25
    n = n - (25 * q)
    d = n // 10
    n = n - (10 * d)
    ni = n // 5
    n = n - (5 * ni)
    p = n // 1
    print(q, d, ni, p)
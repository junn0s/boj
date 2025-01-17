n = int(input())
for _ in range(n):
    a, b, c, d, aa, bb, cc, dd = map(int, input().split())
    a += aa
    b += bb
    c += cc
    d += dd
    if a < 1:
        a = 1
    if b < 1:
        b = 1
    if c < 0:
        c = 0
    print(a + 5*b + 2*c + 2*d)
# 캠핑

import sys
input = sys.stdin.readline

i = 0
while True:
    i += 1
    l, p, v = map(int, input().split())
    if l == 0 and p == 0 and v == 0:
        break
    else:
        a = v // p
        b = v % p
        if b > l: b = l
        print(f"Case {i}: {l * a + b}")
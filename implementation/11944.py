n, m = input().split()

if len(n) * int(n) > int(m):
    a = int(m) // len(n)
    b = int(m) % len(n)
    if b == 0:
        res = n * a
    else:
        res = n * a
        for i in range(b):
            res += n[i]
    print(res)
else:
    res = n * int(n)
    print(res)
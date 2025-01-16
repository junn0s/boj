k, n, m = map(int, input().split())
total = k * n
get = total - m

if get > 0:
    print(get)
else:
    print(0)
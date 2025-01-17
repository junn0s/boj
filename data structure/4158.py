import sys
input = sys.stdin.readline

while True:
    n,m = map(int, input().split())
    if n == 0 and m == 0:
        break
    arr_n = []
    arr_m = []
    for _ in range(n):
        arr_n.append(int(input()))
    for _ in range(m):
        arr_m.append(int(input()))
    set_n = set(arr_n)
    set_m = set(arr_m)

    count = 0
    if len(set_n) < len(set_m):
        for item in set_n:
            if item in set_m:
                count += 1
    else:
        for item in set_m:
            if item in set_n:
                count += 1

    print(count)
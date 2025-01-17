N = int(input())
arr = list(map(int, input().split()))
T, P = map(int, input().split())

num = 0
for item in arr:
    if item <= T:
        if item != 0:
            num += 1
    else:
        a = item // T
        b = item % T
        if b != 0:
            a += 1
        num += a

P1 = N // P
P2 = N % P

print(num)
print(P1, P2)
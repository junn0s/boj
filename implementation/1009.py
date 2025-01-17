T = int(input())

for _ in range(T):
    a, b = map(int, input().split())
    b = (b % 4) + 4
    value = a ** b % 10
    if value == 0:
        value += 10
    print(value)
n = int(input())
for _ in range(n):
    a,b,c = map(float, input().split())
    res = a*b*c
    print("$%.2f" % res)
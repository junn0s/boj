# 지능형 기차2

num = 0
res = []
for _ in range(10):
    a, b = map(int, input().split())
    num -= a
    num += b
    res.append(num)

print(max(res))
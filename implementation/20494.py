# 스시

n = int(input())
res = []
for _ in range(n):
    s = input()
    res.append(len(s))

print(sum(res))
# 수들의 합

s = int(input())
res = 0
for i in range(1, s+1):
    s -= i
    if s <= i:
        res += 1
        break
    else:
        res += 1

print(res)

def combination(n,r):
    temp1 = 1
    for i in range(n, n-r, -1):
        temp1 *= i
    temp2 = 1
    for j in range(1, r+1):
        temp2 *= j
    res = temp1 // temp2
    return res


R, C, W = map(int, input().split())
a = R-1
b = C-1
res = 0
for i in range(a, a+W):
    for j in range(b, i-a+b+1):
        res += combination(i, j)

print(res)
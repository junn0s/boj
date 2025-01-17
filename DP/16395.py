def combination(n,r):
    temp1 = 1
    for i in range(n, n-r, -1):
        temp1 *= i
    temp2 = 1
    for j in range(1, r+1):
        temp2 *= j
    res = temp1 // temp2
    return res



n,k = map(int, input().split())
print(combination(n-1, k-1))
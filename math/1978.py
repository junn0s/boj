def primenum(num):
    if num == 1:
        return 0
    for i in range(2, num):
        if num % i == 0:
            return 0
    return num
        
        
N = int(input())
arr = list(map(int, input().split()))

res = 0
for num in arr:
    if primenum(num) == 0:
        continue
    else:
        res += 1
        
print(res)
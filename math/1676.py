def fact(n):
    res = 1
    for i in range(1, n+1, 1):
        res *= i
    return res

fac = list(str(fact(int(input()))))

res = 0
for item in fac[::-1] :
    if item == '0':
        res += 1
    else : break
    
    
print(res)
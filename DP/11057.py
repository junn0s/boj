MOD = 10007

n = int(input())

arr = []
temp = 10
for _ in range(n):
    arr.append(temp)
    temp += 1
    
product = 1
for num in arr:
    product = (product * num) % MOD
    
factorial = 1
for i in range(1, n + 1):
    factorial = (factorial * i) % MOD
    
result = (product * pow(factorial, MOD - 2, MOD)) % MOD

print(result)

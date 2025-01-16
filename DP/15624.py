def fibo(n):
    a = 0; b = 1
    if n == 0:
        return a
    if n == 1:
        return b
    
    for _ in range(2, n+1):
        c = (a + b) % 1000000007
        a = b
        b = c
        
    return c


n = int(input())
print(fibo(n))
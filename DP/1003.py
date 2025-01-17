def fibonacci(n):
    arr = [[0, 0] for _ in range(n+3)]
    fibo = [0] * (n+3)
    fibo[0] = 0; fibo[1] = 1
    arr[0][0] += 1; arr[1][1] += 1
    
    for i in range(2, n + 1):
        fibo[i] = fibo[i-1] + fibo[i-2]
        arr[i][0] = arr[i-1][0] + arr[i-2][0]
        arr[i][1] = arr[i-1][1] + arr[i-2][1]
        
    print(arr[n][0], arr[n][1])
    

T = int(input())
for _ in range(T):
    fibonacci(int(input()))
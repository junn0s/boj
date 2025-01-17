def house(arr, n):
    for i in range(0, n):
        arr[i+1] = arr[i] + arr[i+1]
    return arr

T = int(input())
for _ in range(T):
    k = int(input())
    n = int(input())
    arr = [i for i in range(1, 15)]
    for _ in range(k):
        house(arr, n-1)
    print(arr[n-1])
    
    
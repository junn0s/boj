# 피보나치 수 5
# 0 1 1 2 3 5 8 13

import sys

def fibo(arr, n):
    for i in range(2, n+1):
        arr[i] = arr[i-1] + arr[i-2]
    return arr[n]

n = int(input())
if n == 0:
    print(0)
    sys.exit()
elif n == 1:
    print(1)
    sys.exit()

arr = [0 for _ in range(n+1)]
arr[0] = 0; arr[1] = 1
print(fibo(arr, n))
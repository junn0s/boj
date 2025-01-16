import sys
input = sys.stdin.readline

n = int(input())
arr = []
for _ in range(n):
    tmp = int(input())
    arr.append(tmp)
    
arr.sort()

tmp = arr[0] * n
for i in range(1, n):
    if tmp < arr[i] * (n-i):
        tmp = arr[i] * (n-i)

print(tmp)
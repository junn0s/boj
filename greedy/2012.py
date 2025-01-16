import sys
input = sys.stdin.readline

n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))
arr.sort()

res = 0
for i in range(n):
    res += abs((i+1) - arr[i])
    
print(res)
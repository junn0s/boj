import sys

n = int(input())
k = int(input())
arr = list(map(int, input().split()))
if k > n:
    print(0)
    sys.exit()
    
arr.sort()
tmp = []
for i in range(n-1):
    tmp.append(arr[i+1] - arr[i])
tmp.sort()
for _ in range(k-1):
    if tmp:
        tmp.pop()
res = sum(tmp)
print(res)
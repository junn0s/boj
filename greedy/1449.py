import sys
input = sys.stdin.readline

n, l = map(int, input().split())
arr = list(map(int, input().split()))

arr.sort()

cnt = 1
tmp = arr[0]
for i in range(1, n):
    if tmp + l - 1 >= arr[i]:
        continue
    else:
        tmp = arr[i]
        cnt += 1
        
print(cnt)
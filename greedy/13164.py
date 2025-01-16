import sys
input = sys.stdin.readline

n, k = map(int, input().split())
arr = list(map(int, input().split()))
new_arr = []

for i in range(n-1):
    tmp = arr[i+1] - arr[i]
    new_arr.append(tmp)
    
new_arr.sort()    
cnt = n-k
sum = 0
for i in range(cnt):
    sum += new_arr[i]
    
print(sum)
import sys
input = sys.stdin.readline


k = int(input())
arr = list()
for _ in range(k):
    temp = int(input().rstrip())
    if temp == 0 and arr:
        arr.pop()
    else:
        arr.append(temp)
        
print(sum(arr))

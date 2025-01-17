import sys
input = sys.stdin.readline


n = int(input())
arr = list()
for _ in range(n):
    temp = list(map(int, input().rstrip().split()))
    arr.append(temp)
    

res = []
for item in arr:
    weight = item[0]
    height = item[1]
    rank = 1
    for item in arr:
        if weight < item[0] and height < item[1]:
            rank += 1
    res.append(rank)
    
    
for i in range(n):
    if i == n-1:
        print(res[i])
    else:
        print(res[i], end=' ')
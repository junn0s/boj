N, M = map(int, input().split())
arr = list()

for _ in range(N):
    temp = list(input())
    temp.reverse()
    arr.append(temp)
    
for row in arr:
    print("".join(map(str, row)))
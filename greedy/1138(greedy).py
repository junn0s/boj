#Greedy Algorithm

N = int(input())
line = list(map(int, input().split()))
arr = [0 for _ in range(N)]

for i in range(0, len(line)):
    location = line[i]
    count = 0
    for j in range(0, len(arr)):
        if arr[j] == 0:
            count += 1
        if count > location:
            break
    arr[j] = i + 1
    
    
print(*arr)

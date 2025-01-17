arr = []
for i in range(1, 46):
    for _ in range(i):
        arr.append(i)
        
a, b = map(int, input().split())
res = sum(arr[a-1:b])
print(res)
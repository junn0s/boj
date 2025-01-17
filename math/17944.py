n, t = map(int, input().split())
tmp = t % ((n*2-1)*2)
arr = []
for i in range(1, n*2):
    arr.append(i)
for i in range(n*2, 1, -1):
    arr.append(i)

print(arr[tmp-1])
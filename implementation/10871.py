N, X = map(int, input().split())
arr = list(map(int, input().split()))

temp = []

for i in range(N):
    if arr[i] < X:
        temp.append(arr[i])

for item in temp:
    print(item, end=' ')
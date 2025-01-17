n,m = map(int, input().split())
arrA = []
arrB = []
for _ in range(n):
    temp = list(map(int, input().split()))
    arrA.append(temp)
for _ in range(n):
    temp = list(map(int, input().split()))
    arrB.append(temp)

res = [[0 for _ in range(m)] for _ in range(n)]
for i in range(0, n):
    for j in range(0, m):
        res[i][j] = arrA[i][j] + arrB[i][j]
        
for item in res:
    for num in item:
        print(num, end=' ')
    print()
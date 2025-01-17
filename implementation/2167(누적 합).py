'''
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = []
for _ in range(n):
    temp = list(map(int, input().split()))
    arr.append(temp)
    
    
k = int(input())
for _ in range(k):
    i, j, x, y = map(int, input().split())
    sum = 0
    for a in range(i-1, x):
        for b in range(j-1, y):
            sum += arr[a][b]
    print(sum)
'''    
    
    
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

# prefix 배열 생성 (1-based 인덱싱을 위해 크기 +1)
prefix = [[0]*(m+1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, m+1):
        prefix[i][j] = arr[i-1][j-1] + prefix[i-1][j] + prefix[i][j-1] - prefix[i-1][j-1]

k = int(input())
for _ in range(k):
    i, j, x, y = map(int, input().split())
    # sub_sum 구하기 (1-based 인덱스 기준)
    sub_sum = prefix[x][y] - prefix[i-1][y] - prefix[x][j-1] + prefix[i-1][j-1]
    print(sub_sum)
# 사과나무

# 조건 1) 오직 정사각형으로만 가능
# 조건 2) 이익은 음수와 양수가 있으며 총이익이 최대가 돼야 함

# 1) 누적합 배열을 만든다
# 2) for문으로 1,2,3..칸 왼쪽에 있는 값들을 빼면서 내려온다


import sys
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

prefix_arr = [[0 for _ in range(n+1)] for _ in range(n+1)]
for i in range(n):
    for j in range(n):
        prefix_arr[i+1][j+1] = arr[i][j] + prefix_arr[i+1][j] + prefix_arr[i][j+1] - prefix_arr[i][j]

cost = -1000
for x in range(1, n+1):
    for i in range(x, n+1):
        for j in range(x, n+1):
            cost = max(cost, prefix_arr[i][j] - prefix_arr[i][j-x] - prefix_arr[i-x][j] + prefix_arr[i-x][j-x])

print(cost)
        
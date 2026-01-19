# 뱀

# 0 0 0 0 0 0
# 0 0 0 0 2 0
# 0 0 0 2 0 0
# 0 0 0 0 0 0
# 0 0 2 0 0 0
# 0 0 0 0 0 0

import sys
from collections import deque
input = sys.stdin.readline

# 입력받기
n = int(input())
k = int(input())
apple = [list(map(int, input().split())) for _ in range(k)]
l = int(input())
change = [list(input().split()) for _ in range(l)]

# 보드와 사과 채우기
board = [[0 for _ in range(n)] for _ in range(n)]
for r, c in apple:
    board[r-1][c-1] = 2

# 시간 및 방향, row, column, d 기본값 할당
time = 0
direction = [(0,1), (1,0), (0,-1), (-1,0)]
d = 0

# 뱀 좌표
snake = deque([(0,0)])
board[0][0] = 1

top_row, top_column = 0,0
change_idx = 0

while True:
    time += 1
    nr = top_row + direction[d][0]
    nc = top_column + direction[d][1]

    # 벽 충돌
    if not (0 <= nr < n and 0 <= nc < n):
        print(time)
        break

    # 몸 충돌
    if board[nr][nc] == 1:
        print(time)
        break

    snake.append((nr, nc))

    # 사과로 인한 꼬리 처리
    if board[nr][nc] == 2:
        board[nr][nc] = 1
    else:
        board[nr][nc] = 1
        tr, tc = snake.popleft()
        board[tr][tc] = 0

    top_row, top_column = nr, nc

    # 방향전환
    if change_idx < l and time == int(change[change_idx][0]):
        if change[change_idx][1] == 'D':
            d = (d+1) % 4
        else:
            d = (d-1) % 4
        change_idx += 1



# 경사로


# 가로를 먼저 보고, 세로를 보면서 판단한다
# 최대 10000회여서 시간은 부족하지 않음

# 조건
# 1. 한 줄이 모두 동일하면 가능
# 2. 경사로를 놓아야 할 상황일 때, 1만큼 더 작으며 L이상 연속되어야 함
# 3. 이미 경사로를 놓은 칸은 건드릴 수 없음


import sys
from collections import deque
input = sys.stdin.readline

n, l = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

def check(line, l):
    used = [False] * n

    for i in range(n-1):
        if line[i] == line[i+1]:
            continue

        diff = line[i+1] - line[i]

        if abs(diff) >= 2:
            return False
        
        if diff == -1:
            for k in range(i+1, i+l+1):
                if k >= n: return False
                if used[k] == True: return False
                if line[k] != line[i+1]: return False

            for k in range(i+1, i+l+1):
                used[k] = True
        
        elif diff == 1:
            for k in range(i, i-l, -1):
                if k < 0: return False
                if used[k] == True: return False
                if line[k] != line[i]: return False

            for k in range(i, i-l, -1):
                used[k] = True

    return True
    

count = 0

for r in range(n):
    if check(board[r], l):
        count += 1

for c in range(n):
    line = [ board[r][c] for r in range(n)]
    if check(line, l):
        count += 1

print(count)









        
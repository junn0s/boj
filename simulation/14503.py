# 로봇 청소기

# 청소기 방향이 있음, 0=북, 1=동, 2=남, 3=서
# 각 칸은 벽 혹은 빈칸
# 가장 왼쪽 위가 0,0 

# 지금 칸 청소 안됐으면 청소
# 주변 4칸이 모두 청소된 경우 바라보는 방향 그대로 뒤로 후진하고 1번으로 돌아감. 벽이면 멈춤
# 주변 4칸중 청소 안된칸 있으면 왼쪽부터 그 칸으로 이동. 방향도 그 방향으로 바꿈

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
r, c, d = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
clean = 0

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

while True:
    if arr[r][c] == 0:
        arr[r][c] = 2
        clean += 1
    
    flag = False
    for _ in range(4):
        d = (d + 3) % 4
        nr = r + dr[d]
        nc = c + dc[d]

        if arr[nr][nc] == 0:
            r, c = nr, nc
            flag = True
            break
    
    if not flag:
        back = (d + 2) % 4
        br = r + dr[back]
        bc = c + dc[back]

        if arr[br][bc] == 1:
            break

        r, c = br, bc

print(clean)
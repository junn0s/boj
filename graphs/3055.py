# 탈출

import sys
from collections import deque
input = sys.stdin.readline

R, C = map(int, input().split())
map = [input().rstrip() for _ in range(R)]

water_position = []
Sx, Sy = 0, 0

for i in range(R):
    for j in range(C):
        if map[i][j] == '*': water_position.append((i, j))
        elif map[i][j] == 'S': Sx, Sy = i, j


wq = deque(water_position)   
hq = deque([(Sx, Sy)])
dist = [[-1]*C for _ in range(R)]
dist[Sx][Sy] = 0
grid = [list(row) for row in map]  

while hq:
    for _ in range(len(wq)):
        x,y = wq.popleft()
        for dx,dy in ((-1, 0), (1, 0), (0, 1), (0, -1)):
            nx,ny = x+dx, y+dy
            if 0 <= nx < R and 0 <= ny < C and grid[nx][ny] == '.':
                grid[nx][ny] = '*'
                wq.append((nx,ny))

    for _ in range(len(hq)):
        x,y = hq.popleft()
        for dx,dy in ((-1, 0), (1, 0), (0, 1), (0, -1)):
            nx,ny = x+dx, y+dy
            if not 0 <= nx < R or not 0 <= ny < C or dist[nx][ny] != -1: continue
            if grid[nx][ny] == 'D':
                print(dist[x][y] + 1); exit()
            if grid[nx][ny] == '.':  
                dist[nx][ny] = dist[x][y] + 1
                hq.append((nx,ny))

print("KAKTUS")
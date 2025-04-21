# 전투 1303

from collections import deque

n, m = map(int, input().split())
arr = [input() for _ in range(m)]
visited = [[False] * n for _ in range(m)]

def bfs(x, y, color):
    q = deque()
    q.append((x, y))
    visited[x][y] = True
    count = 1
    while q:
        x, y = q.popleft()
        for dx, dy in ((-1,0), (1,0), (0,-1), (0,1)):
            nx, ny = x + dx, y + dy
            if 0 <= nx < m and 0 <= ny < n:
                if not visited[nx][ny] and arr[nx][ny] == color:
                    visited[nx][ny] = True
                    q.append((nx, ny))
                    count += 1
    return count

w_total, b_total = 0, 0
for i in range(m):
    for j in range(n):
        if not visited[i][j]:
            color = arr[i][j]
            power = bfs(i, j, color)
            if color == 'W':
                w_total += power ** 2
            else:
                b_total += power ** 2

print(w_total, b_total)
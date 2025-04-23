# 음식물 피하기

from collections import deque

n, m, k = map(int, input().split())
arr = [[0] * m for _ in range(n)]
for _ in range(k):
    r, c = map(int, input().split())
    arr[r-1][c-1] = 1
visited = [[False] * m for _ in range(n)]

def bfs(x, y):
    q = deque()
    q.append((x, y))
    visited[x][y] = True
    count = 1
    while q:
        x, y = q.popleft()
        for dx, dy in ((-1,0), (1,0), (0,-1), (0,1)):
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m:
                if not visited[nx][ny] and arr[nx][ny] == 1:
                    visited[nx][ny] = True
                    q.append((nx, ny))
                    count += 1
    return count

resarr = []
for i in range(n):
    for j in range(m):
        if not visited[i][j] and arr[i][j] == 1:
            tmp = bfs(i, j)
            resarr.append(tmp)

resarr.sort()
print(resarr[len(resarr)-1])
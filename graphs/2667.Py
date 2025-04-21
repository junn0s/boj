# 단지번호붙이기

from collections import deque

n = int(input())
arr = [input() for _ in range(n)]
visited = [[False] * n for _ in range(n)]

def bfs(x, y):
    q = deque()
    q.append((x, y))
    visited[x][y] = True
    count = 1
    while q:
        x, y = q.popleft()
        for dx, dy in ((-1,0), (1,0), (0,-1), (0,1)):
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n:
                if not visited[nx][ny] and arr[nx][ny] == '1':
                    visited[nx][ny] = True
                    q.append((nx, ny))
                    count += 1
    return count

resarr = []
for i in range(n):
    for j in range(n):
        if not visited[i][j] and arr[i][j] == '1':
            tmp = bfs(i, j)
            resarr.append(tmp)

resarr.sort()
print(len(resarr))
for item in resarr:
    print(item)
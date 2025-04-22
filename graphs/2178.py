# 미로 탐색

from collections import deque

n, m = map(int, input().split())
arr = [list(map(int, list(input().strip()))) for _ in range(n)]
visited = [[False] * m for _ in range(n)]

def bfs(x, y):
    q = deque()
    q.append((x, y))
    visited[x][y] = True

    while q:
        x, y = q.popleft()
        for dx, dy in ((-1,0), (1,0), (0,1), (0,-1)):
            nx, ny = x+dx, y+dy
            if 0 <= nx < n and 0 <= ny < m:
                if not visited[nx][ny] and arr[nx][ny] == 1:
                    visited[nx][ny] = True
                    arr[nx][ny] = arr[x][y] + 1
                    q.append((nx, ny))

bfs(0,0)
print(arr[n-1][m-1])
    
'''
bfs 원리
1. 해당 좌표를 큐에 넣고 방문 표시
2. 큐가 존재하는 동안 좌표를 큐에서 빼고 상하좌우 탐색 후 경로 존재 시 큐에 넣음
3. 넣어진 좌표가 여러개면 큐에서 해당 좌표들을 다시 순서대로 빼고 탐색 반복
4. 이 방법으로 넓혀가면서 (너비 우선 탐색) 실행됨

문제 원리
1. (0,0)부터 (n-1,m-1)까지 최단 거리가 필요
2. (0,0)에서 bfs를 돌리면 됨
3. 상하좌우 탐색 후 값이 1이면 미로 배열의 해당 값에 1을 더해서 경로 누적
'''


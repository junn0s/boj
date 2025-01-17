'''import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def dfs(x, y):
    visited[x][y] = True
    
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < N and 0 <= ny < M:
            if field[nx][ny] == 1 and visited[nx][ny] == False:
                dfs(nx, ny)
            

T = int(input())
for _ in range(T):
    M, N, K = map(int, input().split())
    field = [[0] * M for _ in range(N)]
    visited = [[False] * M for _ in range(N)]
    
    for _ in range(K):
        y, x = map(int, input().split())
        field[x][y] = 1
        
    count = 0
    for i in range(N):
        for j in range(M):
            if field[i][j] == 1 and visited[i][j] == False:
                dfs(i, j)
                count += 1
    print(count)
    '''
    
    
    
    
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

T = int(input().strip())
for _ in range(T):
    M, N, K = map(int, input().split())  # M: 가로(열), N: 세로(행)
    
    # 1) 밭과 방문 배열 준비
    field = [[0]*M for _ in range(N)]
    visited = [[False]*M for _ in range(N)]
    
    # 2) 배추 위치 입력 (x, y) → field[y][x] = 1
    for _ in range(K):
        x, y = map(int, input().split())
        field[y][x] = 1
    
    # 3) DFS 정의
    def dfs(r, c):
        visited[r][c] = True
        # 상, 하, 좌, 우
        for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
            nr, nc = r + dr, c + dc
            # 범위 체크
            if 0 <= nr < N and 0 <= nc < M:
                if field[nr][nc] == 1 and not visited[nr][nc]:
                    dfs(nr, nc)
    
    # 4) 전체 grid 순회하며 배추 덩어리(연결 요소) 개수 계산
    count = 0
    for i in range(N):        # i: 행
        for j in range(M):    # j: 열
            if field[i][j] == 1 and not visited[i][j]:
                dfs(i, j)
                count += 1
    
    print(count)

from collections import deque

def angel_escape(n, m, t, grid):
    # 방향벡터 (상, 하, 좌, 우)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    # 방문 여부: (x, y, energy, time)
    visited = set()
    queue = deque([(0, 0, 0, 0)])  # (x, y, energy, time)
    
    while queue:
        x, y, energy, time = queue.popleft()
        
        # 도착지점에 도달한 경우
        if (x, y) == (n-1, m-1):
            return energy  # 최소 에너지 반환
        
        # 시간이 초과된 경우
        if time > t:
            continue
        
        # 현재 상태 방문 처리
        visited.add((x, y, energy, time))
        
        # 현재 위치가 땅(2)이라면 에너지 충전
        if grid[x][y] == 2:
            energy = min(energy + 1, t)  # 최대 k로 제한
        
        # 다음 이동 가능한 방향으로 탐색
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            
            # 범위를 벗어나거나 장애물(0)인 경우
            if not (0 <= nx < n and 0 <= ny < m) or grid[nx][ny] == 0:
                continue
            
            # 하늘(1)로 이동하면 에너지 소모
            next_energy = energy - 1 if grid[nx][ny] == 1 else energy
            
            # 에너지가 음수가 되면 이동 불가
            if next_energy < 0:
                continue
            
            # 방문하지 않은 상태라면 큐에 추가
            next_state = (nx, ny, next_energy, time + 1)
            if next_state not in visited:
                queue.append(next_state)
    
    # 탈출 불가능한 경우
    return -1

# 입력 처리
n, m, t = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# 결과 출력
print(angel_escape(n, m, t, grid))

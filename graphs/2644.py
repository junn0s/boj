import sys
from collections import deque
input = sys.stdin.readline


n = int(input())
a, b = map(int, input().split())
m = int(input())

graph = [[] for _ in range(n+1)]
for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

dist = [-1] * (n+1)
queue = deque([a])
dist[a] = 0

while queue:
    u = queue.popleft()
    for v in graph[u]:
        if dist[v] == -1:
            dist[v] = dist[u] + 1
            queue.append(v)

print(dist[b])




      
# graph = [[] for _ in range(n+1)]
# for _ in range(m):
#     x, y = map(int, input().split())
#     graph[x].append(y)
#     graph[y].append(x)          # 양방향 저장


# distance = [-1] * (n+1)         # 방문 체크 & 거리 저장
# queue = deque([a])              # 두 사람 중 첫 사람을 시작점으로 잡음
# distance[a] = 0                 # 자기 자신은 0촌임

# while queue:
#     u = queue.popleft()         # 방문중인 노드 u
#     for v in graph[u]:          # 이웃 노드들 v
#         if distance[v] == -1:   # 방문 안한경우
#             distance[v] = distance[u] + 1
#             queue.append(v)

# print(distance[b])



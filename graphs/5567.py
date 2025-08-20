import sys
from collections import deque
input = sys.stdin.readline


n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]
for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

dist = [-1] * (n+1)
queue = deque([1])
dist[1] = 0

while queue:
    u = queue.popleft()
    for v in graph[u]:
        if dist[v] == -1:
            dist[v] = dist[u] + 1
            queue.append(v)

cnt = 0
for i in range(2, n+1):
    if dist[i] == 1 or dist[i] == 2:
        cnt += 1

print(cnt)
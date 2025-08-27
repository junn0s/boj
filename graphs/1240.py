import sys
from collections import deque
input = sys.stdin.readline


n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    x, y, d = map(int, input().split())
    graph[x].append((y, d))
    graph[y].append((x, d))

for _ in range(m):
    a, b = map(int, input().split())
    dist = [-1] * (n+1)
    queue = deque([a])
    dist[a] = 0

    while queue:
        u = queue.popleft()
        for v in graph[u]:
            if dist[v[0]] == -1:
                dist[v[0]] = v[1] + dist[u]
                queue.append(v[0])

    print(dist[b])


# 2 (1,2)
# 1 (2,2)
# 4 (3,2)
# 3 (4,2)
# 4 (1,3)
# 1 (4,3)
# 2->1->4->3

# [1]
#  (4,3)

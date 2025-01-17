n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

visited = dict()
for num in arr:
    visited[num] = False
path = []

def dfs(depth):
    if depth == m:
        print(*path)
        return
    for i in arr:
        if not visited[i]:
            path.append(i)
            visited[i] = True
            dfs(depth+1)
            visited[i] = False
            path.pop()


dfs(0)
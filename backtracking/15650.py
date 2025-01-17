n, m = map(int, input().split())
    
visited = [False] * n
path = []

def dfs(start, depth):
    if depth == m:
        print(*path)
        return
    for i in range(start, n+1):
        if not visited[i-1]:
            path.append(i)
            visited[i-1] = True
            dfs(i+1, depth+1)
            visited[i-1] = False
            path.pop()


dfs(1, 0)
                
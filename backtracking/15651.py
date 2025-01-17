n, m = map(int, input().split())
    
path = []

def dfs(depth):
    if depth == m:
        print(*path)
        return
    for i in range(1, n+1):
        path.append(i)
        dfs(depth+1)
        path.pop()

dfs(0)
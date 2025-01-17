n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

visited = dict()
for num in arr:
    visited[num] = False
path = []

def dfs(start, depth):
    if depth == m:
        print(*path)
        return
    for i in range(start, n):
        if not visited[arr[i]]:
            path.append(arr[i])
            visited[arr[i]] = True
            dfs(i+1, depth+1)
            visited[arr[i]] = False
            path.pop()


dfs(0, 0)
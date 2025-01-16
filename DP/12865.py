def knapsack(W, n, weights, values):
    K = [[0 for _ in range(n+1)] for _ in range(W+1)]
    for x in range(W+1):
        K[x][0] = 0
    for i in range(n+1):
        K[0][i] = 0
        
    for x in range(1, W+1):
        for j in range(1, n+1):
            K[x][j] = K[x][j-1]
            if weights[j-1] <= x:
                K[x][j] = max(K[x][j], K[x - weights[j-1]][j-1] + values[j-1])
    
    return K[W][n]

n, k = map(int, input().split())
weights = []
values = []
for _ in range(n):
    w, v  = map(int, input().split())
    weights.append(w)
    values.append(v)
    
print(knapsack(k, n, weights, values))
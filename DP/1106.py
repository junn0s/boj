import sys
input = sys.stdin.readline

def hotel(W, n, weights, values):
    INF = float('inf')
    K = [INF] * (W + 101)
    K[0] = 0
    for x in range(1, W + 101):
        for i in range(n):
            if weights[i] <= x:
                K[x] = min(K[x], K[x - weights[i]] + values[i])
    
    min_value = min(K[W:W + 101])
    return min_value if min_value != INF else -1


W, n = map(int, input().rstrip().split())
values = []
weights = []
for _ in range(n):
    v, w = map(int, input().rstrip().split())
    values.append(v)
    weights.append(w)
    
print(hotel(W, n, weights, values))
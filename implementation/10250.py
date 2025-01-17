T = int(input())

for _ in range(T):
    H, W, N = map(int, input().split())
    
    if N % H == 0:
        X = (N // H)
    else:
        X = (N // H) + 1
        
    if X < 10:
        X = '0' + str(X)
    else:
        X = str(X)
        
    Y = N % H
    if Y == 0:
        Y = H
        Y = str(Y)
    else:
        Y = str(Y)
    print(Y+X)
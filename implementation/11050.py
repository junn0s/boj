# 이항 계수 1

N, K = map(int, input().split())


def combination(N, K):
    N_num = 1
    for i in range(N, (N - K), -1):
        N_num *= i
    
    K_num = 1
    for i in range(1, K+1):
        K_num *= i
        
    result = int(N_num / K_num)
    return result


print(combination(N, K))
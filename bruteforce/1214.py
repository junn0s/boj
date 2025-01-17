import sys
input = sys.stdin.readline

def bruteforce(D, P, Q):
    if D % P == 0 or D % Q == 0: 
        return D

    P, Q = max(P, Q), min(P, Q) 
    max_P = D // P + 1 
    answer = P * max_P 

    for i in range(max_P-1, -1, -1): 
        div, mod = divmod((D - (i * P)), Q) 
        if mod == 0:
            return D 
        min_i = (i * P) + ((div + 1) * Q) 
        if answer == min_i: 
            break 
        answer = min(answer, min_i)

    return answer


D, P, Q = map(int, input().split())
result = bruteforce(D, P, Q)
print(result)
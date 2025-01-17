from collections import deque

def card(num):
    dq = deque(range(1, num + 1))
    while len(dq) > 1:
        dq.popleft()      
        dq.append(dq.popleft()) 
    return dq[0]

N = int(input())
print(card(N))
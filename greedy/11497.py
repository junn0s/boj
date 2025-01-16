import sys
from collections import deque
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    dq = deque(arr)
    left_dq = deque()
    right_dq = deque()
    mod = 0
    while dq:
        if mod % 2 == 0:
            tmp = dq.popleft()
            left_dq.append(tmp)
            mod += 1
        else:
            tmp = dq.popleft()
            right_dq.appendleft(tmp)
            mod += 1
            
    new_dq = left_dq + right_dq
    
    tmp = abs(new_dq[0] - new_dq[1])
    for i in range(1, n-1):
        if abs(new_dq[i] - new_dq[i+1]) > tmp:
            tmp = abs(new_dq[i] - new_dq[i+1])
            
    print(tmp)
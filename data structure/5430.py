import sys
from collections import deque
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    p = input().rstrip()
    n = int(input())
    str_arr = input().rstrip()
    arr = eval(str_arr)
    dq = deque(arr)
    
    reverse = 0
    res = 0
    for item in p:
        if item == 'R':
            reverse += 1
        else:
            if reverse % 2 == 0 and dq:
                dq.popleft()
            elif reverse % 2 == 1 and dq:
                dq.pop()
            else:
                print('error')
                res += 1
                break
    
    if res == 0:
        if reverse % 2 == 1:
            dq.reverse()
        print("[" + ",".join(map(str, dq)) + "]")
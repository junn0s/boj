import sys
from collections import deque
input = sys.stdin.readline
# 2 2 3 3 4 4  
# 4 6 10 8 18 
n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))
    
arr.sort()
arr = deque(arr)
dq = deque()

tmp = arr.popleft()
if arr:
    tmp2 = arr.popleft()
else:
    print(tmp)

dq.append(tmp+tmp2)

while arr:
    dq_tmp = dq.pop()
    arr_tmp = arr.popleft()
    if arr:
        arr_tmp2 = arr.popleft()
        if dq_tmp + arr_tmp < arr_tmp2 + arr_tmp:
            dq.append(dq_tmp)
            dq.append(dq_tmp + arr_tmp)
            arr.appendleft(arr_tmp2)
        else:
            dq.append(dq_tmp)
            dq.append(arr_tmp2 + arr_tmp)
            dq.append(dq_tmp + arr_tmp2 + arr_tmp)
    else:
        dq.append(dq_tmp)
        dq.append(dq_tmp + arr_tmp)
        
res = sum(dq)
print(res)
# 요세푸스 문제 0

from collections import deque

def Josephus(queue:deque, K):
    arr = list()
    i = 1
    while queue:
        if i % K != 0:
            queue.append(queue.popleft())
        else:
            arr.append(queue.popleft())
        i += 1
    
    return arr
        
    


N, K = map(int, input().split())
queue = deque()
for i in range(1, N+1):
    queue.append(i)
    
arr = Josephus(queue, K)

print("<", end='')
for i in range(N-1):
    print(arr[i], end=', ')
print(arr[N-1], end='')
print(">")
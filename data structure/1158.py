#요세푸스 문제

import sys
from collections import deque

input = sys.stdin.readline
N, K = map(int, input().split())

stack = deque()
new_stack = deque()
res = deque()

seq = 0

for i in range(1, N+1):
    stack.append(i)


while stack:
    for num in stack:
        seq += 1
        new_stack.append(num)
        if seq == K:
            seq = 0
            res.append(new_stack.pop())
    stack = new_stack.copy()
    new_stack.clear()
    
    
print("<" + ", ".join(map(str, res)) + ">")




from collections import deque

N, K = map(int, input().split())

stack = deque(range(1, N+1))
res = []

while stack:
    stack.rotate(-(K-1))  # K-1만큼 왼쪽으로 이동
    res.append(stack.popleft())  # K번째 요소 제거

print("<" + ", ".join(map(str, res)) + ">")
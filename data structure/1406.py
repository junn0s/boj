import sys
from collections import deque
input = sys.stdin.readline

left = deque(input().rstrip())  
right = deque()                
n = int(input())

for _ in range(n):
    query = input().rstrip()
    if query == 'L': 
        if left:
            right.appendleft(left.pop())
    elif query == 'D':  
        if right:
            left.append(right.popleft())
    elif query == 'B':  
        if left:
            left.pop()
    elif len(query) == 3:  
        left.append(query[2])


print(''.join(left) + ''.join(right))




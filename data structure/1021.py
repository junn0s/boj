import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
queue = deque()
for i in range(n):
    queue.append(i+1)
tmp = deque(map(int, input().split()))

count = 0
while tmp:
    temp = tmp[0]
    if queue[0] == temp:
        queue.popleft()
        tmp.popleft()
    else:
        idx = queue.index(temp)
        left_rotations = idx
        right_rotations = len(queue) - idx
        if left_rotations < right_rotations:
            queue.rotate(-left_rotations)
            count += left_rotations
        else:
            queue.rotate(right_rotations)
            count += right_rotations
            
print(count)
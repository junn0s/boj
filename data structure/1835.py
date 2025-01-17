from collections import deque

n = int(input())
card = deque()

while n >= 1:
    card.appendleft(n)
    card.rotate(n)
    n -= 1
    
print(*card)
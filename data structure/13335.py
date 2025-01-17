import sys
from collections import deque
input = sys.stdin.readline


n, w, l = map(int, input().split())
trucks = deque(map(int, input().split()))
time = 0
current_weight = 0
bridge = deque([0]*w)  

while trucks or current_weight > 0:
    time += 1
    left_truck = bridge.popleft()
    current_weight -= left_truck
    
    if trucks:
        if current_weight + trucks[0] <= l:
            next_truck = trucks.popleft()
            bridge.append(next_truck)
            current_weight += next_truck
        else:
            bridge.append(0)
    else:
        bridge.append(0)

print(time)
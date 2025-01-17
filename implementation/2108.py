import sys
import math
from collections import deque
input = sys.stdin.readline


def count(list:deque):
    countarr = [0] * 8001
    for item in list:
        countarr[item + 4000] += 1
    
    max_val = max(countarr)
    temp = []
    for i in range(8001):
        if countarr[i] == max_val:
            temp.append(i - 4000)
    
    if len(temp) > 1:
        return temp[1]
    else:
        return temp[0]
    
    
    
list = deque()
N = int(input())
for _ in range(N):
    temp = int(input().rstrip())
    list.append(temp)
    
list = sorted(list)
max_val = list[N-1]
min_val = list[0]

avg = round(sum(list) / N)
mid = list[N//2]
frq = count(list)
range = max_val - min_val

print(avg)
print(mid)
print(frq)
print(range)

# 덱 2

from collections import deque
import sys
input = sys.stdin.readline

def mydeque(arr:deque, n:int, x=0):
    if n == 1:
        arr.appendleft(x)
    elif n == 2:
        arr.append(x)
    elif n == 3:
        if arr: print(arr.popleft()) 
        else: print(-1)
    elif n == 4:
        if arr : print(arr.pop())
        else : print(-1)
    elif n == 5:
        print(len(arr))
    elif n == 6:
        if arr: print(0)
        else: print(1)
    elif n == 7:
        if arr: print(arr[0])
        else: print(-1)
    elif n == 8:
        if arr: print(arr[-1])
        else: print(-1)

n = int(input())
arr = deque()
for _ in range(n):
    query = input().split()
    q = int(query[0])
    if len(query) > 1:
        x = int(query[1])
    else:
        x = 0     
    mydeque(arr, q, x)

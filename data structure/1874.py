import sys
from collections import deque
input = sys.stdin.readline


n = int(input())
arr = []
for _ in range(n):
    temp = int(input())
    arr.append(temp)


def stack_calculate(arr, n):
    j = 1
    i = 0
    result = deque()
    stack = deque()
    while j <= n+1:
        if stack and stack[-1] == arr[i]:
            stack.pop()
            result.append('-')
            i += 1
        else:
            if j <= n:
                stack.append(j)
                result.append('+')
            j += 1
            
    if len(stack) == 0:
        for i in range(len(result)):
            print(result.popleft())
    else:
        print("NO")
    


stack_calculate(arr, n)
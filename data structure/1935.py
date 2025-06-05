import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
arr = input().rstrip()   
values = {}

for i in range(n):
    val = float(input().rstrip())
    values[ chr(ord('A') + i) ] = val

stack = deque()
for ch in arr:
    if 'A' <= ch <= 'Z':
        stack.append(values[ch])
    else:
        b = stack.pop()
        a = stack.pop()
        if ch == '+':
            stack.append(a + b)
        elif ch == '-':
            stack.append(a - b)
        elif ch == '*':
            stack.append(a * b)
        else:  # '/'
            stack.append(a / b)

res = stack.pop()
print(f"{res:.2f}")
# 단어 뒤집기 2

import sys
input = sys.stdin.readline

from collections import deque

s = input().rstrip()
tmp_stack = deque()
res_stack = deque()
flag = True

for i in range(len(s)):
    if s[i] == '<':
        while tmp_stack:
            res_stack.append(tmp_stack.pop())
        res_stack.append(s[i])
        flag = False
    elif s[i] == ' ' and flag:
        while tmp_stack:
            res_stack.append(tmp_stack.pop())
        res_stack.append(s[i])
    elif s[i] == '>':
        while tmp_stack:
            res_stack.append(tmp_stack.popleft())
        res_stack.append(s[i])
        flag = True
    else:
        tmp_stack.append(s[i])

while tmp_stack:
    res_stack.append(tmp_stack.pop())


print(''.join(res_stack))    

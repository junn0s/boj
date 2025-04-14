# 괄호의 값
# () = 2, [] = 3
# (()) = 2*2 , ([]) = 2*3

brackets = list(input())
stack = []
for item in brackets:
    if stack:
        tmp = stack.pop()
    stack.append(item)
    12=


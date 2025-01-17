#스택 사용의 대표적인 예제

import sys
from collections import deque
input = sys.stdin.readline



def balance(string):
    stack = deque()
    for item in string:
        if item == '(' or item == '[':
            stack.append(item)
        elif item == ')':
            if stack:
                temp = stack.pop()
                if temp != '(':
                    print("no")
                    stack.append(temp)
                    return
            else:
                print("no")
                return
        elif item == ']':
            if stack:
                temp = stack.pop()
                if temp != '[':
                    print("no")
                    stack.append(temp)
                    return
            else:
                print("no")
                return
            
    if stack:
        print("no")
        return
    
    print("yes")
        
        
        
        
    
while True:
    string = input().rstrip()
    if string == '.':
        break
    balance(string)
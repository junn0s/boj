# 팰린드롬수

import sys
input = sys.stdin.readline

def palindrome(arr:list):
    num = len(arr) // 2
    ans = 0
    for _ in range(num):
        first = arr.pop(0)
        end = arr.pop()
        if first != end:
            ans += 1
            break
    
    if ans == 1:
        print("no")
    else:
        print("yes")
        

true = True  
while true:
    arr = list()
    num = input().rstrip()
    if num == '0':
        break
    
    for item in num:
        arr.append(item)
        
    palindrome(arr)
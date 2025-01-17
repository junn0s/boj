def stack(arr):
    temp = []
    for i in range(len(arr)):
        if arr[i] == '(':
            temp.append(arr[i])
        else:
            if not temp:
                print("NO")
                return
            temp.pop()
    if temp:
        print("NO")
    else:
        print("YES")
        
        
import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    arr = list(input().rstrip())
    stack(arr)
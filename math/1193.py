#구현 - 분수찾기
#O(n)으로 풀어야 함


import sys
input = sys.stdin.readline

x = int(input().rstrip())

num = 0
count = 0
top_line = 0

for i in range(1, x+1):
    num += i
    if num >= x:
        top_line = num
        count = i
        break
    
bottom_line = top_line - count + 1

if x == 1:
    top = 1
    bottom = 1
elif count % 2 != 0:
    top = count - (x - bottom_line)
    bottom = count - top + 1
else:
    top = 1 + (x - bottom_line)
    bottom = count - top + 1
    
    
print(f"{top}/{bottom}")
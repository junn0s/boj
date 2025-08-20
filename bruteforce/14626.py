# ISBN

import sys
input = sys.stdin.readline

isbn = input().rstrip()

num = 0
index = 0
for i in range(12):
    if isbn[i] == '*':
        index = i
    elif i % 2 == 0:
        num += int(isbn[i])
    else:
        num += int(isbn[i]) * 3

num += int(isbn[12])
num %= 10

if index % 2 == 0:
    print(10 - num)
else:
    print((num * 3) % 10)
# 명령 프롬프트

import sys
input = sys.stdin.readline

n = int(input())
arr = []
for _ in range(n):
    file_name = input().rstrip()
    arr.append(file_name)

res = ''
for j in range(len(file_name)):
    flag = 0
    src = arr[0][j]
    for i in range(1, n):
        tmp = arr[i][j]
        if src != tmp:
            flag = 1
    if flag == 1:
        res += '?'
    else:
        res += src

print(res)
        

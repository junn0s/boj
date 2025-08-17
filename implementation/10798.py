#세로읽기

import sys
input = sys.stdin.readline

arr = [['#' for _ in range(15)] for _ in range(5)]
for i in range(5):
    tmp = input().rstrip()
    for j in range(len(tmp)):
        arr[i][j] = tmp[j]

for j in range(15):
    for i in range(5):
        if arr[i][j] == '#':
            continue
        else:
            print(arr[i][j], end='')


# 지피티 버전..
words = [input().rstrip() for _ in range(5)]
max_len = max(len(w) for w in words)
for i in range(max_len):
    for w in words:
        if i < len(w):
            print(w[i], end='')
#닉네임에 갓 붙이기

import sys
input = sys.stdin.readline


n = int(input())
for _ in range(n):
    name = list(input().split())
    name[0] = 'god'
    print("".join(name))

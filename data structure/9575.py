# 행운의 수

import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    a = set(a)
    m = int(input())
    b = list(map(int, input().split()))
    b = set(b)
    k = int(input())
    c = list(map(int, input().split()))
    c = set(c)
    res = set()
    for i in a:
        for j in b:
            for l in c:
                temp = i + j + l
                num = str(temp)
                for u in num:
                    if u != '5' and u != '8':
                        break
                else:
                    res.add(int(num))
    print(len(res))
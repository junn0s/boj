#주사위 네개

import sys
input = sys.stdin.readline

n = int(input())
prize = 0
for _ in range(n):
    tmp = list(map(int, input().split()))
    tmp.sort()
    if len(set(tmp)) == 1:
        prize = max(prize, 50000 + tmp[0] * 5000)
    elif len(set(tmp)) == 2:
        if tmp[0] == tmp[2] or tmp[1] == tmp[3]:
            prize = max(prize, 10000 + tmp[1] * 1000)
        else:
            prize = max(prize, 2000 + tmp[0]*500 + tmp[2]*500)
    elif len(set(tmp)) == 3:
        for i in range(3):
            if tmp[i] == tmp[i+1]:
                prize = max(prize, 1000 + tmp[i] * 100)
                break
    else:
        prize = max(prize, tmp[3]*100)

print(prize)

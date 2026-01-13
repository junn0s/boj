# 롤러코스터

# 홀 홀 : 무조건 전부 지나감 r->d->l->d / 마지막 r
# 홀 짝 : 홀 홀과 동일
# 짝 홀 : 무조건 전부 지나감 d->r->u->r / 마지막 d
# 짝 짝 : 
# - 1) (r+c)가 홀수인 칸 중 최소값 위치를 찾음(i, j)
# - 2) 최소값 위치와 인접한 한 줄을 같이 묶음(i가 짝수면 아랫줄, i가 홀수면 윗줄을 같이 묶음)
# - 3) 묶인 것 이전 위쪽은 r->d->l->d
# - 4) 묶은 것은 d->r->u->r..  만약 u타이밍에 막혀있다면 r을 한번 더, d타이밍에 막혀있어도 r을 한번 더.. 마지막에 d를 2번
# - 5) 남은 것은 l->d / 이후 r->d->l->d / 마지막 r

# 1 1 1 1 1 1 1 1
# 1 1 1 1 1 1 1 1
# 1 1 1 1 1 0 1 1
# 1 1 1 1 0 1 1 1
# 1 1 1 1 1 1 1 1
# 1 1 1 1 1 1 1 1


import sys
input = sys.stdin.readline

r, c = map(int, input().split())
arr = list()

for _ in range(r): 
    tmp = list(map(int, input().split()))
    arr.append(tmp)

if r % 2 == 1:
    move = ('R' * (c-1) + 'D' + 'L' * (c-1) + 'D') * (r//2) + 'R' * (c-1)
    print(move)
elif c % 2 == 1:
    move = ('D' * (r-1) + 'R' + 'U' * (r-1) + 'R') * (c//2) + 'D' * (r-1)
    print(move)
else:
    move = ''
    fr, fc = 0, 1
    mn = arr[0][1]
    for i in range(r):
        for j in range(c):
            if (i+j) % 2 == 1 and arr[i][j] < mn:
                mn = arr[i][j]
                fr, fc = i, j
    
    r0 = (fr // 2) * 2
    move += ('R' * (c-1) + 'D' + 'L' * (c-1) + 'D') * (r0//2)

    x = 0
    y = 0
    mid = []
    while y < c - 1:
        if x == 0:
            if fr == r0 + 1 and fc == y:
                move += 'R'; y += 1
            else:
                move += 'D'; x = 1
                move += 'R'; y += 1
        else:
            if fr == r0 and fc == y:
                move += 'R'; y += 1
            else:
                move += 'U'; x = 0
                move += 'R'; y += 1

    if x == 0:
        move += 'D'
        x = 1

    for i in range(r0 + 2, r, 2):
        move += ('D' + 'L' * (c - 1) + 'D' + 'R' * (c - 1))

    print(move)


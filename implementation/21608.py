# 상어 초등학교
# TODO: 로직이 더러워서 고쳐야 할 듯

import sys
input = sys.stdin.readline

n = int(input())
arr = [] # 학생 배열
for _ in range(n**2):
    tmp = list(map(int, input().split()))
    arr.append(tmp)

classroom = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n**2):
    # 현재 학생
    current_student = arr[i][0]
    # 그 학생의 가장 친한 친구 4명 (집합)
    best_friend = []
    for m in range(1, 5):
        best_friend.append(arr[i][m])
    best_friend = set(best_friend)

    # 1번 조건
    firstcount = [] # 인접 칸에 있는 친한 친구 수 배열
    count = 0
    for j in range(n):
        for k in range(n):
            if j-1 >= 0 and classroom[j-1][k] in best_friend: count += 1
            if j+1 < n and classroom[j+1][k] in best_friend: count += 1
            if k-1 >= 0 and classroom[j][k-1] in best_friend: count += 1
            if k+1 < n and classroom[j][k+1] in best_friend: count += 1

            if classroom[j][k] != 0:  # 이미 해당 교실 위치에 자리 있는 경우
                firstcount.append(-1)
            else:
                firstcount.append(count)
            count = 0

    # 1 조건을 만족하는 칸이 여러 개인지 확인
    max = 0 
    index = [] # 해당 칸 인덱스
    for num in range(n**2):
        if firstcount[num] > max: max = firstcount[num] # 친한친구 가장 많은 경우
    for i in range(n**2):
        if firstcount[i] == max: index.append(i)
    
    # 1번 조건 만족하는 경우
    if len(index) == 1:
        r = index[0] // n
        c = index[0] % n
        classroom[r][c] = current_student

    # 1번 만족하는 게 여러 개라 2번 조건으로 넘어감
    else:
        secondcount = [] # 인접칸 중 빈칸개수 배열
        count = 0
        for item in index:
            r = item // n
            c = item % n
            if r-1 >= 0 and classroom[r-1][c] == 0: count += 1
            if r+1 < n and classroom[r+1][c] == 0: count += 1
            if c-1 >= 0 and classroom[r][c-1] == 0: count += 1
            if c+1 < n and classroom[r][c+1] == 0: count += 1
            secondcount.append([count, item])
            count = 0

        # 2조건이 만족하는 칸이 여러 개인지 확인
        max = 0
        index = []
        for num in range(len(secondcount)):
            if secondcount[num][0] > max: max = secondcount[num][0] # 빈칸 가장 많은경우
        for i in range(len(secondcount)):
            if secondcount[i][0] == max: index.append(secondcount[i][1])

        # 2번 조건 만족하는 경우
        if len(index) == 1:
            r = index[0] // n
            c = index[0] % n
            classroom[r][c] = current_student

        # 3번 조건으로 넘어감
        else:
            r = index[0] // n  # 인덱스 순이므로 작은쪽이 행과 열 둘다 작음
            c = index[0] % n
            classroom[r][c] = current_student


# 만족도구하기
res = 0
for j in range(n):
    for k in range(n):
        current_student = classroom[j][k]
        best_friend = []
        for i in range(len(arr)):
            if arr[i][0] == current_student: 
                best_friend.append(arr[i][1])
                best_friend.append(arr[i][2])
                best_friend.append(arr[i][3])
                best_friend.append(arr[i][4])
        count = 0
        if j-1 >= 0 and classroom[j-1][k] in best_friend: count += 1
        if j+1 < n and classroom[j+1][k] in best_friend: count += 1
        if k-1 >= 0 and classroom[j][k-1] in best_friend: count += 1
        if k+1 < n and classroom[j][k+1] in best_friend: count += 1

        if count == 0: res += 0
        elif count == 1: res += 1
        elif count == 2: res += 10
        elif count == 3: res += 100
        else: res += 1000

print(res)
# 빙고

import sys
input = sys.stdin.readline

bingo = [list(input().split()) for _ in range(5)]
tmp = [list(input().split()) for _ in range(5)]

nums = []
for i in range(5):
    for j in range(5):
        nums.append(tmp[i][j])

res_count = 0
for num in nums:
    res_count += 1
    for i in range(5):
        for j in range(5):
            if bingo[i][j] == num:
                bingo[i][j] = 'X'
    if res_count > 11:
        bingo_count = 0
        for i in range(5):
            row_count = 0
            for j in range(5):
                if bingo[i][j] == 'X': row_count += 1
            if row_count == 5:
                bingo_count += 1
        for j in range(5):
            col_count = 0
            for i in range(5):
                if bingo[i][j] == 'X': col_count += 1
            if col_count == 5:
                bingo_count += 1
        if bingo[0][0] == 'X' and bingo[1][1] == 'X' and bingo[2][2] == 'X' and bingo[3][3] == 'X' and bingo[4][4] == 'X':
            bingo_count += 1
        if bingo[0][4] == 'X' and bingo[1][3] == 'X' and bingo[2][2] == 'X' and bingo[3][1] == 'X' and bingo[4][0] == 'X':
            bingo_count += 1
        if bingo_count >= 3:
            print(res_count)
            break
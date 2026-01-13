# 킹

# 전형적인 쉬운 시뮬레이션 문제
# 킹이 돌을 밀고감
# 체스판 바깥으로 나갈 경우에는 그 이동은 건너 뜀(킹과 돌 모두 적용)

import sys
input = sys.stdin.readline


move_dict = {"R":[1,0], "L":[-1,0], "B":[0,-1], "T":[0,1], "RT":[1,1], "LT":[-1,1], "RB":[1,-1], "LB":[-1,-1]}

king, stone, n = input().split()
king = str(ord(king[0]) - 64) + king[1]
stone = str(ord(stone[0]) - 64) + stone[1]

for _ in range(int(n)):
    move = input().rstrip()
    move = move_dict[move]

    king_column = int(king[0]) + move[0]
    king_row = int(king[1]) + move[1]
    stone_column = int(stone[0]) + move[0]
    stone_row = int(stone[1]) + move[1]

    if 0 < king_column < 9 and 0 < king_row < 9:
        if king_column == int(stone[0]) and king_row == int(stone[1]):
            if 0 < stone_column < 9 and 0 < stone_row < 9:
                king = str(king_column) + str(king_row)
                stone = str(stone_column) + str(stone_row)
        else:
            king = str(king_column) + str(king_row)

king = chr(int(king[0]) + 64) + king[1]
stone = chr(int(stone[0]) + 64) + stone[1]
print(king)
print(stone)
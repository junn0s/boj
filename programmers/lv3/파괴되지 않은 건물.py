# prefix_sum 문제로 접근해보자
# +1 -1 기법 적용 (차분 배열)

def solution(board, skill):
    n, m = len(board), len(board[0])
    arr = [[0] * (m + 1) for _ in range(n + 1)]

    # 차분 배열
    for type, r1, c1, r2, c2, degree in skill:
        if type == 1:
            degree = -degree
        arr[r1][c1] += degree
        arr[r1][c2 + 1] -= degree
        arr[r2 + 1][c1] -= degree
        arr[r2 + 1][c2 + 1] += degree

    # 가로 누적합
    for i in range(n):
        for j in range(m):
            arr[i][j+1] += arr[i][j]

    # 세로 누적합
    for j in range(m):
        for i in range(n):
            arr[i+1][j] += arr[i][j]

    # 원본에 반영
    res = 0
    for i in range(n):
        for j in range(m):
            board[i][j] += arr[i][j]
            if board[i][j] > 0:
                res += 1

    return res




# 보드 크기 3x3
# 5 5 5
# 5 5 5
# 5 5 5
# 차분 배열 초기 4x4
# 0 0 0 0
# 0 0 0 0
# 0 0 0 0
# 0 0 0 0
# 스킬 기록
# -2 0  2 0 
#  0 0  0 0
#  2 0 -2 0
#  0 0  0 0
# 누적 합(가로)
# -2 -2 0 0
#  0  0 0 0
#  2  2 0 0
#  0  0 0 0
# 누적 합(세로)
# -2 -2 0 0
# -2 -2 0 0
#  0  0 0 0
#  0  0 0 0
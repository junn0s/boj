# 제곱수 찾기

import sys, math
input = sys.stdin.readline

n, m = map(int, input().split())
board = [input().strip() for _ in range(n)]

max_square = -1

for i in range(n):
    for j in range(m):
        for dr in range(-n, n):
            for dc in range(-m, m):
                if dr == 0 and dc == 0:
                    continue  # 무한 루프 방지

                r, c = i, j
                num_str = ""
                while 0 <= r < n and 0 <= c < m:
                    num_str += board[r][c]
                    num = int(num_str)
                    root = int(math.isqrt(num))
                    if root * root == num:
                        max_square = max(max_square, num)
                    r += dr
                    c += dc

print(max_square)
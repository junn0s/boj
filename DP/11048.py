# 이동하기

'''
문제 정의
- 2차원 dp 문제
- 아래, 오른쪽, 아래 대각선 이동 가능(총 3개)
- 미로 크기 총 1,000,000 (O(n)만 가능)

아이디어
- dp테이블 업데이트
- 첫 줄 가로 : 그냥 왼쪽 값 현재값에 더함
- 첫 줄 세로 : 그냥 위 값 현재값에 더함
- 나머지(1,1부터) : 왼, 위, 왼 대각선 위 중 가장 큰 값 + 현재값

예제 1 dp테이블
1  3  6  10
1  3  6  15
10 18 25 31
'''

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
maze = []
dp = [[0] * m for _ in range(n)]
for _ in range(n):
    tmp = list(map(int, input().split()))
    maze.append(tmp)

for i in range(m):
    if i == 0:
        dp[0][i] = maze[0][i]
    else:
        dp[0][i] = maze[0][i] + dp[0][i-1]

for i in range(n):
    if i == 0:
        dp[0][i] = maze[0][i]
    else:
        dp[i][0] = maze[i][0] + dp[i-1][0]

if n > 1 and m > 1:
    for i in range(1, n):
        for j in range(1, m):
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-1], dp[i][j-1]) + maze[i][j]

print(dp[n-1][m-1])

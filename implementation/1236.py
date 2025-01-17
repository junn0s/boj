N, M = map(int, input().split())
castle = [list(input()) for _ in range(N)]

row_num = 0
column_num = 0

for i in range(N):
    if 'X' not in castle[i]:
        row_num += 1

for i in range(M):
    column = [castle[j][i] for j in range(N)]
    if 'X' not in column:
        column_num += 1

result = max(row_num, column_num)
print(result)

def chessboard(board, x, y):
    count1 = 0
    count2 = 0
    for i in range(8):
        for j in range(8):
            if (i + j) % 2 == 0:
                if board[x + i][y + j] != 'W':
                    count1 += 1
                if board[x + i][y + j] != 'B':
                    count2 += 1
            else:
                if board[x + i][y + j] != 'B':
                    count1 += 1
                if board[x + i][y + j] != 'W':
                    count2 += 1
    return min(count1, count2)

def loop(board, M, N):
    min_repaints = float('inf')
    for i in range(M - 7):
        for j in range(N - 7):
            repaints = chessboard(board, i, j)
            if repaints < min_repaints:
                min_repaints = repaints
    return min_repaints


M, N = map(int, input().split())
board = []
for _ in range(M):
    arr = input()
    board.append(arr)
    
result = loop(board, M, N)
print(result)
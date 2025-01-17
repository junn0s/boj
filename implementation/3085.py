import sys
input = sys.stdin.readline

def count_max_candies(board, n):
    max_count = 1
    
    for i in range(n):
        count = 1
        for j in range(1, n):
            if board[i][j] == board[i][j-1]:
                count += 1
            else:
                count = 1
            max_count = max(max_count, count)
    
    for j in range(n):
        count = 1
        for i in range(1, n):
            if board[i][j] == board[i-1][j]:
                count += 1
            else:
                count = 1
            max_count = max(max_count, count)
    
    return max_count

n = int(input().strip())
board = [list(input().strip()) for _ in range(n)]  
answer = count_max_candies(board, n)  

for i in range(n):
    for j in range(n):
        if j + 1 < n:
            board[i][j], board[i][j+1] = board[i][j+1], board[i][j]
            answer = max(answer, count_max_candies(board, n))
            board[i][j], board[i][j+1] = board[i][j+1], board[i][j]

        if i + 1 < n:
            board[i][j], board[i+1][j] = board[i+1][j], board[i][j]
            answer = max(answer, count_max_candies(board, n))
            board[i][j], board[i+1][j] = board[i+1][j], board[i][j]

print(answer)
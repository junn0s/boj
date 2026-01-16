# 틱택토

# 조건 
# 1) x가 2개 이상 더 많은 경우 불가능
# 2) o가 x보다 더 많은 경우 불가능
# 3) o로 완성되지 않았는 경우 x = 5, o = 4 가능
# 4) .이 하나라도 있는경우 x가 o보다 1개 더 많고 x는 완성되고 o는 완성되지 않은 경우 가능
# 5) .이 하나라도 있는 경우 x와 o 개수가 같고 o는 완성되고 x는 완성되지 않은 경우 가능

import sys
input = sys.stdin.readline

def check_x(tictaktoe):
    flag = False
    for i in range(3):
        if tictaktoe[i][0] == 'X' and tictaktoe[i][1] == 'X' and tictaktoe[i][2] == 'X':
            flag = True
        if tictaktoe[0][i] == 'X' and tictaktoe[1][i] == 'X' and tictaktoe[2][i] == 'X':
            flag = True
    
    if tictaktoe[0][0] == 'X' and tictaktoe[1][1] == 'X' and tictaktoe[2][2] == 'X':
        flag = True
    if tictaktoe[0][2] == 'X' and tictaktoe[1][1] == 'X' and tictaktoe[2][0] == 'X':
        flag = True
    
    return flag

def check_o(tictaktoe):
    flag = False
    for i in range(3):
        if tictaktoe[i][0] == 'O' and tictaktoe[i][1] == 'O' and tictaktoe[i][2] == 'O':
            flag = True
        if tictaktoe[0][i] == 'O' and tictaktoe[1][i] == 'O' and tictaktoe[2][i] == 'O':
            flag = True
    
    if tictaktoe[0][0] == 'O' and tictaktoe[1][1] == 'O' and tictaktoe[2][2] == 'O':
        flag = True
    if tictaktoe[0][2] == 'O' and tictaktoe[1][1] == 'O' and tictaktoe[2][0] == 'O':
        flag = True
    
    return flag

while True:
    board = input().rstrip()
    if board == 'end':
        break

    top = list(board[0:3])
    mid = list(board[3:6])
    bottom = list(board[6:9])

    tictaktoe = []
    tictaktoe.append(top)
    tictaktoe.append(mid)
    tictaktoe.append(bottom)

    count_x = 0
    count_o = 0
    count_dot = 0

    for state in board:
        if state == 'X':
            count_x += 1
        elif state == 'O':
            count_o += 1
        else:
            count_dot += 1
    
    if count_dot:
        if count_x == count_o + 1:
            if check_x(tictaktoe) and not check_o(tictaktoe):
                print("valid")
                continue
        elif count_x == count_o:
            if check_o(tictaktoe) and not check_x(tictaktoe):
                print("valid")
                continue
    else:
        if count_x == count_o + 1:
            if not check_o(tictaktoe):
                print("valid")
                continue

    
    print("invalid")




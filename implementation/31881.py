import sys
input = sys.stdin.readline

def infection(index):
    global value
    if arr[index-1] == 0:
        arr[index-1] = 1
        value -= 1

def cure(index):
    global value
    if arr[index-1] == 1:
        arr[index-1] = 0
        value += 1

N, Q = map(int, input().split())
arr = [0 for _ in range(N)]
value = N

for _ in range(Q):
    query = input().split()
    if len(query) > 1:
        case, index = int(query[0]), int(query[1])
    else:
        case = int(query[0])
        
    if case == 1:
        infection(index)
    elif case == 2:
        cure(index)
    elif case == 3:
        print(value)


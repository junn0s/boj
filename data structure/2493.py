# 탑


# 6 2 13 9 5 7 8 4 11

# 6          # 0                      # 1 --> 나보다 왼쪽에 있는 놈 (없으면 0)
# 6 2        # 0 1                    # 1 2
# 13         # 0 1 0                  # 3
# 13 9       # 0 1 0 3                # 3 4
# 13 9 5     # 0 1 0 3 4              # 3 4 5
# 13 9 7     # 0 1 0 3 4 4            # 3 4 6
# 13 9 8     # 0 1 0 3 4 4 4          # 3 4 7
# 13 9 8 4   # 0 1 0 3 4 4 4 7        # 3 4 7 8
# 13 11      # 0 1 0 3 4 4 4 7 3      # 3 9

# 규칙
# 1. 내가 작다면 삽입
# 2. 내가 크다면 나보다 큰 놈 나올때 까지 pop



import sys
input = sys.stdin.readline

n = int(input())
top_stack = list(map(int, input().split()))
height_stack = list()
index_stack = list()
res_stack = list()

for i in range(n):
    while height_stack:
        tmp = height_stack.pop()
        tmp2 = index_stack.pop()
        if top_stack[i] < tmp:
            height_stack.append(tmp)
            height_stack.append(top_stack[i])
            index_stack.append(tmp2)
            index_stack.append(i+1)
            break
    else:
        height_stack.append(top_stack[i])
        index_stack.append(i+1)

    if len(index_stack) > 1:
        res_stack.append(index_stack[-2])
    else:
        res_stack.append(0)


print(*res_stack)
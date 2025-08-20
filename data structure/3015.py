# 오아시스 재결합

import sys
input = sys.stdin.readline

n = int(input())
people_stack = list()
for _ in range(n):
    people_stack.append(float(input()))
height_stack = list()
res_stack = list()

for i in range(n):

    cnt = 0
    while height_stack:
        tmp = height_stack.pop()
        cnt += tmp[1]
        if people_stack[i] < tmp[0]:
            height_stack.append(tmp)
            height_stack.append([people_stack[i], 1])
            res_stack.append(cnt - tmp[1] + 1)
            break
        elif people_stack[i] == tmp[0]:
            if height_stack:
                res_stack.append(cnt + 1)
            else:
                res_stack.append(cnt)
            tmp[1] += 1
            height_stack.append(tmp)
            break
    else:
        res_stack.append(cnt)
        height_stack.append([people_stack[i], 1])

print(sum(res_stack))


# 규칙
# 1. 내가 작거나 같다면 삽입
# 2. 내가 크다면 나보다 같거나 큰 놈 나올때 까지 pop



# 7
# 2 4 1 2 2 5 1
# 2             # 0
# 4             # 1
# 4 1           # 1
# 4 2           # 2
# 4 2(2)        # 2
# 5             # 3
# 5 1           # 1

# 13
# 8 8 7 7 7 6 6 7 7 7 7 9 9
# 8              # 0
# 8(2)           # 1
# 8(2) 7(1)      # 1 - 작은 경우 8자체로
# 8(2) 7(2)      # 2 - 같은경우 7개수 , 8자체
# 8(2) 7(3)      # 3 - 같은경우 7개수(2), 8자체
# 8(2) 7(3) 6(1) # 1 - 작은경우 7자체로
# 8(2) 7(3) 6(2) # 2 - 7자체, 6개수
# 8(2) 7(4)      # 2+3+1 = 6
# 8(2) 7(5)      # 4+1 = 5
# 8(2) 7(6)      # 5+1 = 6
# 8(2) 7(7)      # 6+1 = 7
# 9              # 2+7 = 9
# 9(2)           # 1
# // Answer: 44

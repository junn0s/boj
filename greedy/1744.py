# 수 묶기

# 수를 정렬한다
# 양수 : 1 보다 큰 수는 큰 수들끼리 무조건 묶는다. 1은 묶지 않는다
# 0 : 음수가 없거나 음수 개수가 짝수면 묶지 않는다. 홀수일 경우에만 남는 음수과 묶는다.
# 음수 : 음수의 개수가 짝수이면 작은 음수끼리 묶는다. 홀수이면 남은 1개의 음수는 0이 있다면 0과 곱하고, 0이 없다면 묶지 않는다.


# -1 1 2 3
# 0 1 2 3 4 5
# -1
# -1 0 1
# 1 1

import sys
input = sys.stdin.readline


n = int(input())
number_list = list()
result_list = list()
zero_list = list()
one_list = list()
minus_list = list()
plus_list = list()

for _ in range(n):
    number = int(input())
    number_list.append(number)

number_list.sort()
for number in number_list:
    if number == 0:
        zero_list.append(number)
    elif number == 1:
        one_list.append(number)
    elif number > 1:
        plus_list.append(number)
    else:
        minus_list.append(number)

while len(plus_list) >= 2:
    tmpnum1 = plus_list.pop()
    tmpnum2 = plus_list.pop()
    result_list.append(tmpnum1 * tmpnum2)
if plus_list:
    result_list.append(plus_list[0])

if one_list:
    result_list.append(sum(one_list))

while len(minus_list) >= 2:
    tmpnum1 = minus_list.pop(0)
    tmpnum2 = minus_list.pop(0)
    result_list.append(tmpnum1 * tmpnum2)
if minus_list and not zero_list:
    result_list.append(minus_list[0])

print(sum(result_list))




# 막대기

# 막대 길이 합이 X보다 클 경우, 가진 것 중 가장 짧은 것을 절반으로 자름
# 절반 중 하나를 버렸을 경우에도 막대 길이 합이 X보다 큰 경우 버림
# -> 2진수 만드는 것과 똑같음
# 따라서 비트마스킹으로 변환 후 1인 것 개수만 세면 됨

import sys
input = sys.stdin.readline

x = int(input())
binary_x = bin(x)
res = 0
for item in binary_x:
    if item == '1':
        res += 1

print(res)
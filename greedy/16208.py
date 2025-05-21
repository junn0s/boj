# 귀찮음

import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
arr.sort()

def recursion(sub):
    if len(sub) <= 1:
        return 0
    mid = len(sub) // 2
    left = sub[:mid]
    right = sub[mid:]
    left_sum = sum(left)
    right_sum = sum(right)
    return (left_sum * right_sum) + recursion(left) + recursion(right)

print(recursion(arr))


# n = int(input())
# steel = sorted(list(map(int, input().split())))
# ans = 0
# s = sum(steel)
# for i in range(n):
#     s -= steel[i]
#     ans += steel[i] * s
# print(ans)
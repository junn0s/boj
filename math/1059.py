# 좋은 구간 1059
# 3 7 12 18 25 33 100 1000
# 34 99
# (99-59) + (99-58) * (58-34+1)
# 25 * 41 + 40

import sys

l = int(input())
arr = list(map(int, input().split()))
n = int(input())

if n in arr:
    print(0)
    sys.exit()

arr.sort()
max_num = 0
min_num = 1

for num in arr:
    if num > n:
        max_num = num - 1
        break

for num in arr:
    if num < n:
        min_num = num + 1

res = (max_num - n) + (max_num - (n-1)) * (n-min_num)
print(res)
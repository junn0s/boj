# 뒤집기

import sys
input = sys.stdin.readline

s = input().rstrip()
one = s.split("0")
zero = s.split("1")
one_count = 0
zero_count = 0

for item in one:
    if item: one_count += 1
for num in zero:
    if num: zero_count += 1


print(one)
print(zero)
print(min(one_count, zero_count))

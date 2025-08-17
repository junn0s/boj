# 블로그2

import sys
input = sys.stdin.readline

n = int(input())
prob = input().rstrip()

blue = prob.split('R')
red = prob.split('B')
blue_count = 0
red_count = 0

for item in blue:
    if item: blue_count += 1
for item in red:
    if item: red_count += 1

print(min(blue_count, red_count) + 1)
# 성적통계

import sys
input = sys.stdin.readline

k = int(input())
for i in range(k):
    math = list(map(int, input().split()))
    num = math.pop(0)

    math.sort()
    max_score = math[num-1]
    min_score = math[0]

    gap = 0
    for j in range(num-1):
        gap = max(gap, math[j+1] - math[j])
    largest_gap = gap

    print(f"Class {i+1}")
    print(f"Max {max_score}, Min {min_score}, Largest gap {largest_gap}")




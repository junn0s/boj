# 안녕 2020 안녕 2021

from collections import Counter
import sys
input = sys.stdin.readline

num = set()
num.add(202021)
num.add(20202021)
num.add(202002021)
num.add(202012021)
num.add(202022021)
num.add(202032021)
num.add(202042021)
num.add(202052021)
num.add(202062021)
num.add(202072021)
num.add(202082021)
num.add(202092021)

t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    cnt = Counter(arr)
    result = 0
    used = set()

    for x in cnt:
        for h in num:
            y = h - x
            if y in cnt:
                if x == y:
                    result += cnt[x] * (cnt[x] - 1) // 2
                elif y > x:  # 중복 제거
                    result += cnt[x] * cnt[y]

    print(result)


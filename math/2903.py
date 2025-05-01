# 중앙 이동 알고리즘 2903

n = int(input())
first = 2
for i in range(n):
    first = first * 2 - 1
print(first * first)

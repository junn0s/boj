import itertools

N, M = map(int, input().split())

arr = list(map(int, input().split()))

combinations = itertools.combinations(arr, 3)

temp = []
for combo in combinations:
    if sum(combo) <= M:
        temp.append(sum(combo))

temp.sort()
temp.reverse()
print(temp[0])

    
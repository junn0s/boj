n = int(input())
arr = list(map(int, input().split()))
total = sum(arr) + ((len(arr)-1) * 8)

day = total // 24
hour = total - (day * 24)

print(day, hour)
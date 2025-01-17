import sys
input = sys.stdin.readline

c = int(input())
for _ in range(c):
    arr = list(map(int, input().split()))
    sum = 0
    for i in range(1, len(arr)):
        sum += arr[i]
    if sum == 0:
        res = 0
    else: 
        res = sum / arr[0]
    count = 0
    for i in range(1, len(arr)):
        if arr[i] > res:
            count += 1
    if count == 0:
        res = 0
    else:
        res = 100 * count / arr[0]
    print("%.3f%%" % (res))

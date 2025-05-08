# 버블 정렬 2

import sys
input = sys.stdin.readline

n, k = map(int, input().split())
arr = list(map(int, input().split()))

def bubble(arr, n, k):
    count = 0
    for i in range(n-1, 0, -1):
        for j in range(0, i):
            if arr[j] > arr[j+1]:
                count += 1
                arr[j], arr[j+1] = arr[j+1], arr[j]
            if count == k:
                return arr
    return -1
    

result = bubble(arr, n, k)
if result == -1:
    print(-1)
else:
    print(*result)
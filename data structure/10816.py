import sys
input = sys.stdin.readline

N = int(input())
numarr = list(map(int, input().split()))
M = int(input())
checkarr = list(map(int, input().split()))

numarr.sort()

def leftmost_binary_search(arr, target):
    left, right = 0, len(arr) - 1
    result = -1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            result = mid
            right = mid - 1
        elif arr[mid] > target:
            right = mid - 1
        else:
            left = mid + 1

    return result

def rightmost_binary_search(arr, target):
    left, right = 0, len(arr) - 1
    result = -1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            result = mid
            left = mid + 1
        elif arr[mid] > target:
            right = mid - 1
        else:
            left = mid + 1

    return result

results = []
for num in checkarr:
    left_index = leftmost_binary_search(numarr, num)
    if left_index != -1:
        right_index = rightmost_binary_search(numarr, num)
        count = right_index - left_index + 1
        results.append(count)
    else:
        results.append(0)

print(' '.join(map(str, results)))




# 딕셔너리(hash map)을 사용한 다른 풀이
'''
from sys import stdin

n = stdin.readline().rstrip()
card = list(map(int,stdin.readline().split()))
m = stdin.readline().rstrip()
test = list(map(int,stdin.readline().split()))

hash = {}

for i in card:
    if i in hash:
        hash[i] += 1
    else:
        hash[i] = 1

for i in test:
    if i in hash:
        print(hash[i], end=' ')
    else:
        print(0, end=' ')
'''
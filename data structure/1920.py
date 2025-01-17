import sys
input = sys.stdin.readline

N = int(input())
numarr = list(map(int, input().split()))
M = int(input())
checkarr = list(map(int, input().split()))

numarr.sort()

def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return 1
        elif arr[mid] > target:
            right = mid - 1
        else:
            left = mid + 1

    return 0

for num in checkarr:
    print(binary_search(numarr, num))
import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
prefix_arr = [0] * (n)
prefix_arr[0] = arr[0]

for i in range(1, n):
    prefix_arr[i] = prefix_arr[i-1] + arr[i]
m = int(input())
for _ in range(m):
    a, b = map(int, input().split())
    if a == 1:
        print(prefix_arr[b-1])
    else:
        print(prefix_arr[b-1] - prefix_arr[a-2])
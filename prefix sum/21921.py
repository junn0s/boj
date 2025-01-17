import sys
input = sys.stdin.readline

n, x = map(int, input().split())
arr = list(map(int, input().split()))
window_sum = sum(arr[:x])
max_visit = window_sum
count = 1

for i in range(x, n):
    window_sum = window_sum + arr[i] - arr[i-x]
    if window_sum > max_visit:
        count = 1
        max_visit = window_sum
    elif window_sum == max_visit:
        count += 1
        

if max_visit == 0:
    print("SAD")
else:
    print(max_visit)
    print(count)
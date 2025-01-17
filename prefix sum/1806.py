import sys
input = sys.stdin.readline

def two_pointer_min_length(nums, M):
    n = len(nums)
    left, right = 0, 0
    current_sum = 0
    min_length = float('inf')

    while True:
        if current_sum < M and right < n:
            current_sum += nums[right]
            right += 1
        else:
            if current_sum >= M:
                min_length = min(min_length, right - left)
            if left < n:
                current_sum -= nums[left]
                left += 1
            else:
                break
    
        if right == n and current_sum < M:
            break

    return 0 if min_length == float('inf') else min_length



n, s = map(int, input().split())
nums = list(map(int, input().split()))
print(two_pointer_min_length(nums, s))
import sys
import bisect
input = sys.stdin.readline

n, m = map(int, input().split())
loc_arr = list(map(int, input().split()))
loc_arr.sort()
for _ in range(m):
    start, end = map(int, input().split())
    # 들어갈 수 있는 가장 최소 위치
    start_idx = bisect.bisect_left(loc_arr, start)
    # 들어갈 수 있는 가장 최대 위치
    end_idx = bisect.bisect_right(loc_arr, end) - 1
    print(end_idx - start_idx + 1)

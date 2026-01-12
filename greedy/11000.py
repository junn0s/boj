# 강의실 배정

# 시작 시간으로 정렬
# 강의실 1부터 배정
# 배정 불가능하면 다음 강의실로 배정



import sys
import heapq
input = sys.stdin.readline

n = int(input())
classList = list()

for _ in range(n):
    s, t = map(int, input().split())
    classList.append([s,t])
classList.sort()

heap = []
heapq.heappush(heap, classList[0][1])

for s, t in classList[1:]:
    if heap[0] <= s:         
        heapq.heappop(heap)
        heapq.heappush(heap, t)
    else:                    
        heapq.heappush(heap, t)

print(len(heap))
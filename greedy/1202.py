# 1. 보석 무게 오름차순 정렬
# 2. 가방 무게 오름차순 정렬
# 3. jewels와 bags를 동시에 스캔하며
# 현재 보석이 현재 가방에 들어간다면 push
# 안들어간다면 heappop 후 다음 가방
# 4. 가방이 남았다면 남은 가방갯수만큼 heappop

import sys
import heapq
input = sys.stdin.readline

jewels = []
bags = []

n, k = map(int, input().split())
for _ in range(n):
    m, v = map(int, input().split())
    jewels.append([m,v])
for _ in range(k):
    c = int(input())
    bags.append(c)
    
jewels.sort(key=lambda x:x[0])
bags.sort()

bag_index = 0
jewels_index = 0
tmp_bag = []
heapq.heapify(tmp_bag)
total = 0
while jewels_index < n and bag_index < k:
    if jewels[jewels_index][0] <= bags[bag_index]:
        heapq.heappush(tmp_bag, -jewels[jewels_index][1])
        jewels_index += 1
    else:
        if tmp_bag:
            total += abs(heapq.heappop(tmp_bag))
        bag_index += 1

while bag_index < k and tmp_bag:    
    total += abs(heapq.heappop(tmp_bag))
    bag_index += 1

print(total)
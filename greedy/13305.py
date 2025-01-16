# 나보다 더 작은놈이 나오면 바로 그놈으로 갈아타기 전략

import sys
input = sys.stdin.readline

n = int(input())
distance = list(map(int, input().split()))
price = list(map(int, input().split()))

tmp_price = price[0]
tmp_distance = distance[0]
res_arr = []
for i in range(1, len(price)-1):
    if price[i] < tmp_price:
        res_arr.append(tmp_price * tmp_distance)
        tmp_price = price[i]
        tmp_distance = distance[i]
    else:
        tmp_distance += distance[i]
        
res_arr.append(tmp_price * tmp_distance)
print(sum(res_arr))
# 주식
import sys
input = sys.stdin.readline

T = int(input().strip())
for _ in range(T):
    N = int(input().strip())
    prices = list(map(int, input().split()))
    
    max_price = 0    
    total_profit = 0  

    for i in range(N - 1, -1, -1):
        if prices[i] >= max_price:
            max_price = prices[i]
        else:
            total_profit += max_price - prices[i]

    print(total_profit)
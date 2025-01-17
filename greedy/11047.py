import sys
input = sys.stdin.readline

n, k = map(int, input().rstrip().split())
coinlist = []
for _ in range(n):
    coin = int(input().rstrip())
    coinlist.append(coin)
    
coinlist.sort(reverse=True)
count = 0
for coin in coinlist:
    temp = k // coin
    if temp > 0:
        count += temp
        k -= (temp * coin)
        
print(count)
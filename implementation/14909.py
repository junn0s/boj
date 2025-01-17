import sys
input = sys.stdin.readline


arr = list(map(int, input().split()))
count = 0
for num in arr:
    if num > 0:
        count += 1
        
print(count)
        
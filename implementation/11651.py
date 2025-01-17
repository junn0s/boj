import sys
input = sys.stdin.readline

n = int(input())
arr = list()
for _ in range(n):
    temp = list(map(int, input().rstrip().split()))
    arr.append(temp)
    
arr.sort(key=lambda x: (x[1], x[0]))

for item in arr:
    print(item[0], item[1])
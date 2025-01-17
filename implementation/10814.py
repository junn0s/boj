import sys
input = sys.stdin.readline

N = int(input())
boj = list()
i = 0
for _ in range(N):
    age, name = input().split()
    boj.append([int(age), name, i])
    i += 1
    
    
boj.sort(key=lambda x: (x[0], x[2]))

for entry in boj:
    print(entry[0], entry[1])
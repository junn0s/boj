import sys
input = sys.stdin.readline

log = dict()
arr = list()
n = int(input())

for _ in range(n):
    name, state = input().rstrip().split()
    log[name] = state
    
for name, state in log.items():
    if state == 'enter':
        arr.append(name)
        
arr.sort(reverse=True)
for name in arr:
    print(name)
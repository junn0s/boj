import sys
N = int(input())
arr = list()
for _ in range(N):
    arr.append(sys.stdin.readline().rstrip())
    
new_string = set(arr)
new_string = sorted(new_string, key=lambda x : (len(x), x))

for word in new_string:
    print(word)
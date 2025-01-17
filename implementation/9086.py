import sys
input = sys.stdin.readline

t = int(input().rstrip())
for _ in range(t):
    temp = input().rstrip()
    print(temp[0], end="")
    print(temp[-1])
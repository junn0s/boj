import sys
input = sys.stdin.readline

n = int(input())
s = input().rstrip()

for i in range(n-5, n):
    print(s[i], end='')
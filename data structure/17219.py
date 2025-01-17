import sys
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())
password = dict()

for _ in range(N):
    url, pwd = input().rstrip().split()
    password[url] = pwd
    
for _ in range(M):
    url = input().rstrip()
    print(password[url])
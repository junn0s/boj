import sys 
input = sys.stdin.readline

n,m = map(int, input().rstrip().split())

name = set()
res = list()

for _ in range(n):
	temp = input().rstrip()
	name.add(temp)

for _ in range(m):
	temp = input().rstrip()
	if temp in name:
		res.append(temp)
		
res.sort()
print(len(res))
for item in res:
	print(item)
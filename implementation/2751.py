import sys
input = sys.stdin.readline


N = int(input())
arr = list()

for _ in range(N):
    num = int(input())
    arr.append(num)
    
arr.sort()

for entry in arr:
    print(entry)


# tip : 파이썬 내장함수 sort가 가장 효율적이고 빠르다
# tip : 따라서 이상한 sort 구현하려고 뻘짓 안해도 됨
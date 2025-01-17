import sys
input = sys.stdin.readline

paper = [[0 for _ in range(100)] for _ in range(100)]

num = int(input())
for _ in range(num):
    num1, num2 = map(int, input().split())
    for i in range(num1, num1+10):
        for j in range(num2, num2+10):
            if paper[i][j] == 0:
                paper[i][j] = 1
                
count = 0              
for i in range(100):
    for j in range(100):
        if paper[i][j] == 1:
            count += 1
            
print(count)
# 스타트와 링크


'''
4일때 3가지 경우 나옴 = 4C2 % 2
12-21 / 34-43
13-31 / 24-42
14-41 / 23-32

6일때? 6C3 % 2 = 10가지
각각 3C2 = 3
총 30가지
123 456 / 124 356 / 125 346 / 126 345 /
134 256 / 135 246 / 136 245 /
145 236 / 146 235 / 
156 234

그럼 20일때? 20C10 % 2 = 92378 
각각 10C2 = 45
총 약 50만가지
'''

import sys
from itertools import combinations
input = sys.stdin.readline

n=int(input())

arr=[]
members=[]
for i in range(n):
    tmp = list(map(int, input().split()))
    arr.append(tmp)
    members.append(i)

comb1=list(combinations(members,n//2))

sumList=[]
for x in comb1:
    comb2=list(combinations(x,2))
    tmp=0
    for y in comb2:
        tmp+=arr[y[0]][y[1]]+arr[y[1]][y[0]]

    sumList.append(tmp)


answer=10000000 
for i in range(len(sumList)//2):
    tmp=abs(sumList[i]-sumList[len(sumList)-i-1])
    answer=min(answer,tmp)

print(answer)
# 랜선 자르기

import sys
input = sys.stdin.readline

K, N = map(int, input().split())
arr = list()
sum = 0
for _ in range(K):
    temp = int(input())
    sum += temp
    arr.append(temp)
    

len = sum // K

res = 0
def binary(low, high):
    if high<low:
        return
    global N
    global res
    mid = (low + high) // 2
    temp = 0
    for item in arr:
        temp += item // mid
    if temp >= N:
        res = mid   
        binary(mid+1, high)
    else:
        binary(low, mid-1)    
        
        
binary(0, len*2)
print(res)







################################################################






def binary(low, high, n):
    if high < low:
        return high
    
    mid = (low + high) // 2
    tmp = 0
    for item in arr:
        tmp += item // mid
        
    if tmp >= n: 
        return binary(mid+1, high, n)
    else:
        return binary(low, mid-1, n) 

k, n = map(int, input().split())
arr = []
total = 0
for _ in range(k):
    tmp = int(input())
    total += tmp
    arr.append(tmp)

max_len = total // n
print(binary(1, max_len, n))
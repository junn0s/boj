# PHPPHPHHPHPHPHHHP
# 왼쪽으로 최대한 먼 거 부터, 그 뒤 오른쪽 가장 가까운거

import sys
input = sys.stdin.readline

n, k = map(int, input().split())
arr = input().rstrip()
arr = list(arr)

res = 0
check = True
for i in range(n):
    check = True
    if arr[i] == 'P':
        for j in range(k,0,-1):
            if i-j >= 0 and arr[i-j] == 'H':
                arr[i-j] = 'N'
                res += 1
                check = False
                break
        if check:
            for j in range(1, k+1):
                if i+j < n and arr[i+j] == 'H':
                    arr[i+j] = 'N'
                    res += 1
                    break

print(res)
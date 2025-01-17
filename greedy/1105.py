from collections import deque

L, R = map(str, input().split())
arr_l = deque(list(L))
arr_r = deque(list(R))

total = 0
cnt = len(arr_r) - len(arr_l)
for _ in range(cnt):
    arr_l.appendleft('0')

for i in range(len(arr_r)):
    if arr_l[i] == arr_r[i]:
        if arr_l[i] == '8' and arr_r[i] == '8':
            total += 1
    else:
        break
    
print(total)
h, w = map(int, input().split())
arr = list(map(int, input().split()))
res_arr = []
for i in range(w):
    now = arr[i]
    left_tmp = []
    right_tmp = []
    for j in range(0, i):
        left_tmp.append(arr[j])
    for j in range(i+1, w):
        right_tmp.append(arr[j])
    if left_tmp:
        left = max(left_tmp)
    else:
        left = 0
    if right_tmp:
        right = max(right_tmp)
    else:
        right = 0
    height = min(left, right)
    res = height - now
    if res >= 0:
        res_arr.append(res)
        
        
print(sum(res_arr))
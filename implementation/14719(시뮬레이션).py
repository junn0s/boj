# h, w = map(int, input().split())
# arr = list(map(int, input().split()))
# res_arr = []
# for i in range(w):
#     now = arr[i]
#     left_tmp = []
#     right_tmp = []
#     for j in range(0, i):
#         left_tmp.append(arr[j])
#     for j in range(i+1, w):
#         right_tmp.append(arr[j])
#     if left_tmp:
#         left = max(left_tmp)
#     else:
#         left = 0
#     if right_tmp:
#         right = max(right_tmp)
#     else:
#         right = 0
#     height = min(left, right)
#     res = height - now
#     if res >= 0:
#         res_arr.append(res)
        
        
# print(sum(res_arr))


####################################################
# 빗물
# 아이디어 : 각 세로 블럭 마다 받을 수 있는 빗물 구하기
# 내 기준 왼쪽 최대, 내 기준 오른쪽 최대 구하고, 둘 중 최소 - 현재 내 값 = 받을 수 있는 빗물 양

h, w = map(int, input().split())
arr = list(map(int, input().split()))
resarr = []
for i in range(w):
    now = arr[i]
    left = []
    right = []
    for j in range(0, i):
        left.append(arr[j])
    for j in range(i+1, w):
        right.append(arr[j])
    if left: lh = max(left)
    else: lh = 0
    if right: rh = max(right)
    else: rh = 0
    h = min(lh, rh)
    res = h - now
    if res >= 0:
        resarr.append(res)

print(sum(resarr))
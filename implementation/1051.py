# 숫자 정사각형

'''
접근법
1. 왼쪽 상단 꼭짓점을 잡는다
2. 같은 줄에 같은 값이 있는지 확인 후 오른쪽 상단 꼭짓점을 잡는다
3. 해당 거리가 n, m 중 최솟값보다 크면 no
4. 작거나 같다면 하단 꼭짓점 두 개와 같은 값인지 확인
5. 정사각형이 있다면 크기를 res에 기록, 처음 res=0 이후 크면 업데이트하는 방식(max)

시간복잡도
O(nm^2) = 125000
'''
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
limit = min(n, m)
arr = []
for _ in range(n):
    num = input()
    arr.append(num)

res = 1
for i in range(n):
    for j in range(m):
        val = arr[i][j]
        if j < m-1:
            for k in range(j+1, m):
                if arr[i][k] == val and k - j <= limit:
                    if k - j < n - i:
                        if arr[i+(k-j)][j] == val and arr[i+(k-j)][k] == val:
                            res = max(res, (k-j+1)**2)

print(res)














# res = 1
# for i in range(n):
#     for j in range(m):
#         base = arr[i][j]
#         max_offset = min(limit, n - i, m - j)
#         for d in range(1, max_offset):
#             if arr[i][j + d] != base:
#                 continue
#             if arr[i + d][j] == base and arr[i + d][j + d] == base:
#                 side = d + 1
#                 res = max(res, side * side)






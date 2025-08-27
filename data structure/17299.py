# 오등큰수

import sys
from collections import Counter
input = sys.stdin.readline


n = int(input())
A = list(map(int, input().split()))
A.reverse()

cnt = Counter(A)

stack = []
ans = []
for i in range(n):
    while stack:
        tmp = stack.pop()
        if tmp[1] > cnt[A[i]]:
            stack.append(tmp)
            stack.append([A[i], cnt[A[i]]])
            break
    else:
        stack.append([A[i], cnt[A[i]]])
    
    if len(stack) > 1:
        ans.append(stack[-2][0])
    else:
        ans.append(-1)

ans.reverse()
print(*ans)


# 1 2 4 3 2 1 1
# 뒤에서부터 넣기
# 1[3] -> -1
# 1[3] 2[2] -> 1
# 1[3] 2[2] 4[1] -> 2
# 1[3] 2[2] 3[1] -> 2
# 1[3] 2[2] -> 1
# 1[3] -> -1
# 1[3] -> -1
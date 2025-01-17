import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [i for i in range(1, N+1)]

for _ in range(M):
    i, j = map(int, input().split())
    rotate = j-i+1
    for _ in range(rotate):
        if i <= j:
            arr[i-1], arr[j-1] = arr[j-1], arr[i-1]
            i += 1
            j -= 1
        
print(*arr)



import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [i for i in range(1, N+1)]

for _ in range(M):
    i, j = map(int, input().split())
    # 슬라이싱과 reverse를 사용해 효율적으로 뒤집기
    arr[i-1:j] = arr[i-1:j][::-1]

print(*arr)
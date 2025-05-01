# 1학년
# 5557

n = int(input())
arr = list(map(int, input().split()))
dp = [[0] * 21 for _ in range(n - 1)]
dp[0][arr[0]] = 1

for i in range(1, n - 1):
    for j in range(21):
        if dp[i - 1][j] != 0:
            if j + arr[i] <= 20:
                dp[i][j + arr[i]] += dp[i - 1][j]
            if j - arr[i] >= 0:
                dp[i][j - arr[i]] += dp[i - 1][j]
 
print(dp[n - 2][arr[-1]])

# 아이디어
# 8 -> 3(11, 5) -> 2(13, 9, 7, 3) -> 4(17, 9, 13, 5, 11, 3, 7) -> ...
# 하나씩 더하고 빼면서 나올 수 있는 모든 경우의 수를 dp에 저장한다. (0보다 크고 20보다 작거나 같은 경우들만), 1씩 더함
# dp테이블은 길이 21(0부터 20)로 잡고 n-1개만큼 존재함(2차원 배열)
# 마지막까지 이중 반복문을 돌고, 마지막 값(예제에서는 8) 인 인덱스의 값이 정답임
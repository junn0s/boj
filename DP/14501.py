n = int(input())
arr = []
dp = [0] * (n+1)
for _ in range(n):
    t, p = map(int, input().split())
    arr.append([t, p])
    

#for i in range(n):
#    tmp = arr[i][1]
#    if (i+1) + arr[i][0] <= n:
#        dp[(i+1) + arr[i][0]] = max(dp[(i+1) + arr[i][0]], tmp + dp[i+1])

for i in range(n):
    # (1) 오늘 일을 스킵하는 경우 → i+1일차의 최대 이익 갱신
    dp[i+1] = max(dp[i+1], dp[i])
    
    # (2) 오늘 일을 수행하는 경우
    next_day = i + arr[i][0]  # 일을 끝내고 난 뒤 시작할 수 있는 날
    if next_day <= n:         # n일차 안에서 끝나야 함
        dp[next_day] = max(dp[next_day], dp[i] + arr[i][1])

print(dp)





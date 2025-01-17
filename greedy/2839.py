#첫 DP문제

def min_sugar_bags(N):
    dp = [-1] * (N + 1)
    
    if N >= 3:
        dp[3] = 1
    if N >= 5:
        dp[5] = 1

    for i in range(6, N + 1):
        if dp[i - 3] != -1:
            dp[i] = dp[i - 3] + 1
        if dp[i - 5] != -1:
            dp[i] = min(dp[i], dp[i - 5] + 1) if dp[i] != -1 else dp[i - 5] + 1

    return dp[N]

N = int(input().strip())
print(min_sugar_bags(N))

#############################################################################################

#새로운 방법
N = int(input())

a = N // 5

def loop(a, N):
    temp = N - (5 * a)
    if temp % 3 == 0:
        b = temp // 3
        return (a + b)
    else :
        a -= 1
        if a == -1:
            return (-1)
        return loop(a, N)
    
print(loop(a, N))
import sys
input = sys.stdin.readline

def wine(arr, n):
    if n == 0:
        return arr[0]
    if n == 1:
        return arr[0] + arr[1]
    if n == 2:
        return max(arr[0] + arr[2], arr[1] + arr[2], arr[0] + arr[1])
    
    dp = [0] * (n+1)
    dp[0] = arr[0]
    dp[1] = arr[0] + arr[1]
    dp[2] = max(arr[0] + arr[2], arr[1] + arr[2], arr[0] + arr[1])
    dp[3] = max(dp[1] + arr[3], arr[0] + arr[2] + arr[3])
    
    for i in range(4, n+1):
        dp[i] = max(dp[i-2] + arr[i], dp[i-3] + arr[i-1] + arr[i], dp[i-4] + arr[i-1] + arr[i])
    
    res = max(dp)
    return res


n = int(input())
arr = []
for _ in range(n):
    temp = int(input())
    arr.append(temp)
    
print(wine(arr, n-1))
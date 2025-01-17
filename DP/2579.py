# 직접 푼 DP문제(실패..gpt 도움..)

'''def upstair(arr:list, n):
    if n == 0:
        return arr[0]
    sum = arr[n]
    count = 1
    while n >= 2:
        if arr[n-1] >= arr[n-2]:
            temp = arr[n-1]
            count += 1
            n -= 1
        else:
            temp = arr[n-2]
            count = 1
            n -= 2
            
        if count == 3:
            temp = arr[n-2]
            count = 1
            n -= 1
            
        sum += temp
    
    if n == 1:
        sum += arr[0]
        
    return sum
'''
 
def upstair(arr, n):
    if n == 0:
        return arr[0]
    if n == 1:
        return arr[0] + arr[1]
    
    dp = [0] * (n + 1)
    dp[0] = arr[0]
    dp[1] = arr[0] + arr[1]
    dp[2] = max(arr[0] + arr[2], arr[1] + arr[2])
    
    for i in range(3, n + 1):
        dp[i] = max(dp[i-2] + arr[i], dp[i-3] + arr[i-1] + arr[i])
    
    return dp[n]    
    
n = int(input())
arr = []
for _ in range(n):
    temp = int(input())
    arr.append(temp)
    
print(upstair(arr, n-1))
# 6 16  4 26 27  1 12 25  9 11 18 19 29 23 20  2 22 10  5 28 24  3 21 30 15 13  7 14 17  8
# 1  2  1  3  4  1  2  3  2  3  4  5  6  6  6  2  7  3  3  8  8  3  7  9  4  4  4  5  6  5
import sys
input = sys.stdin.readline

def boxing(arr:list, n):
    dp = [0] * n
    dp[0] = 1
    
    for i in range(1, n):
        dp[i] = 1
        temp = []
        for j in range(0, i):
            if arr[j] < arr[i]:
                temp.append(dp[j])
        if temp:
            dp[i] += max(temp)
        
    return max(dp)

n = int(input())
arr = list(map(int, input().rstrip().split()))
print(boxing(arr, n))
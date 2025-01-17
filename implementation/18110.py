import sys
input = sys.stdin.readline

def custom_round(number):
    if number - int(number) >= 0.5:
        return int(number) + 1
    else:
        return int(number)

def level(arr:list, n):
    if n == 0:
        return 0
    arr.sort()
    num = custom_round(n * 0.15)
    sum = 0
    for i in range(num, n-num, 1):
        sum += arr[i]
    res = custom_round(sum / (n - 2*num))
    return res

n = int(input())
arr = list()
for _ in range(n):
    temp = int(input().rstrip())
    arr.append(temp)

print(level(arr, n))

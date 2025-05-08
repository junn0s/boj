# 생일

n = int(input())
arr = []
for _ in range(n):
    name, dd, mm, yyyy = input().split()
    dd, mm, yyyy = int(dd), int(mm), int(yyyy)
    arr.append([name, dd, mm, yyyy])

arr.sort(key=lambda x:x[1], reverse=True)
arr.sort(key=lambda x:x[2], reverse=True)
arr.sort(key=lambda x:x[3], reverse=True)
print(arr[0][0])
print(arr[-1][0])
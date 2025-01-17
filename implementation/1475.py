import sys
input = sys.stdin.readline

number = str(input().rstrip())
arr = [0 for _ in range(10)]
for num in number:
    index = int(num)
    if index == 9:
        arr[6] += 1
    else:
        arr[index] += 1
        
arr[6] = arr[6] // 2 + arr[6] % 2
print(max(arr))

#################################################################
'''
arr = [[0 for _ in range(10)] for _ in range(6)]

for num in number:
    index = int(num)
    for i in range(6):
        if index == 9 and arr[i][9] == 1 and arr[i][6] == 0:
            arr[i][6] = 1
            break
        elif index == 6 and arr[i][6] == 1 and arr[i][9] == 0:
            arr[i][9] = 1
            break
        else:
            if arr[i][index] == 0:
                arr[i][index] = 1
                break
          
count = 0    
for i in range(6):
    if 1 in arr[i]:
        count += 1       
print(count
'''
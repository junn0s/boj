import sys
input = sys.stdin.readline

while True:
    line = input().strip()
    arr = list(map(int, line.split()))

    if arr[0] == 0:
        break
    
    new_arr = []
    for i in range(1, len(arr)-1):
        if arr[i] != arr[i+1]:
            new_arr.append(arr[i])

    new_arr.append(arr[len(arr)-1])
    new_arr.append('$')
    print(*new_arr)
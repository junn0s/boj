arr = list(map(int, input().split()))

temp1 = sorted(arr)
temp2 = sorted(arr, reverse=True)

if arr == temp1:
    print("ascending")
elif arr == temp2:
    print("descending")
else:
    print("mixed")
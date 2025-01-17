k = int(input())

arr = ["G...",".I.T", "..S."]
new_arr = []

for i in range(3):
    for _ in range(k):
        for j in range(4):
            for _ in range(k):
                new_arr.append(arr[i][j])
    
count = 0
for item in new_arr:
    print(item, end="")
    count += 1
    if count == 4*k:
        print()
        count = 0
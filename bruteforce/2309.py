# 일곱 난쟁이

# 경우의 수 : 36(9C2) -> 브루트포스 적용
# 오름차순으로 출력

arr = []
for _ in range(9):
    h = int(input())
    arr.append(h)

index1, index2 = 0, 0
total = sum(arr)
for i in range(8):
    for j in range(i+1, 9):
        if (total - (arr[i] + arr[j])) == 100:
            index1, index2 = i, j
            break

arr[index1] = 0
arr[index2] = 0
arr.sort()

for item in arr:
    if item == 0:
        continue
    else:
        print(item)
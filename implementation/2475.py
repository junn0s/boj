origin_num = list(map(int, input().split()))
sum = 0

for num in origin_num:
    sum += num ** 2

result_num = sum % 10
print(result_num)
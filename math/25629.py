n = int(input())
arr = list(map(int, input().split()))
count_even = 0
count_odd = 0

for num in arr:
    if num % 2 == 0:
        count_even += 1
    else:
        count_odd += 1
        
if n % 2 == 0:
    if count_odd == count_even:
        print(1)
    else:
        print(0)
else:
    if count_odd == count_even + 1:
        print(1)
    else:
        print(0)

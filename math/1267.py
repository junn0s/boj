N = int(input())
arr = list(map(int, input().split()))

sum_a = 0
sum_b = 0
for item in arr:
    a = 10 * (item // 30 + 1)
    sum_a += a
    b = 15 * (item // 60 + 1)
    sum_b += b

if sum_a > sum_b:
    print("M", sum_b)
elif sum_b > sum_a:
    print("Y", sum_a)
else:
    print("Y M", sum_a)
A = int(input())
B = int(input())
C = int(input())

result = A * B * C
arr = list(str(result))

count = [0] * 10

for num in arr:
    count[int(num)] += 1

for i in range(10):
    print(count[i])
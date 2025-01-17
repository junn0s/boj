arr = []

for _ in range(10):
    num = int(input())
    value = num % 42
    arr.append(value)
    
set = set(arr)
print(len(set))
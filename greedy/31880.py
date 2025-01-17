add = []
mul = []
add_temp = 0
mul_temp = 1

N, M = map(int, input().split())
add = list(map(int, input().split()))
mul = list(map(int, input().split()))

for item in add:
    add_temp += item

for item in mul:
    if item != 0:
        mul_temp *= item
    
result = add_temp * mul_temp
print(result)
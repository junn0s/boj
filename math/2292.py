N = int(input())

a = N // 6
b = N % 6

temp = 0
val = 0
for i in range(1, a+1):
    temp = i * (i+1) / 2
    if a <= temp:
        val = i
        break
    
if a == temp and b > 1:
    val += 1
    
val += 1
print(val)
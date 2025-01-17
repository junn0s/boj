n = int(input())
arr = list(map(int, input().split()))
  
v = int(input())  
num = 0
for item in arr:
    if item == v:
        num += 1
        
print(num)
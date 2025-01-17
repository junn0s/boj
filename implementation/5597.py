arr = [i for i in range(1,31,1)]
temp = []
for _ in range(28):
    num = int(input())
    temp.append(num)
    
for item in temp:
    if item in arr:
        arr.remove(item)
        
arr.sort()

print(arr.pop(0))
print(arr.pop(0))
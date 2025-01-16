def move(n, src, tmp, dest):    
    global num
    global arr
    
    if n == 0 : 
        pass 
    elif n > 0:
        move(n-1, src, dest, tmp)  
        arr.append([src, dest]) 
        num += 1 
        move(n-1, tmp, src, dest)  
 
num = 0
arr = []
n = int(input())
move(n, 1, 2, 3)
print(num)
for item in arr:
    print(*item)
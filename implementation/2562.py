num_arr = []
for _ in range(9):
    temp = int(input())
    num_arr.append(temp)
   
temp = num_arr[0]
value = 1    
for i in range(8):
    if temp < num_arr[i+1]:
        temp = num_arr[i+1]
        value = i+2
        
print(temp)
print(value)
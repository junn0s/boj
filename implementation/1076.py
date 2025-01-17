arr = ['black', 'brown', 'red', 'orange', 'yellow', 
       'green', 'blue', 'violet', 'grey', 'white']

first = input()
second = input()
third = input()

temp = ''
for i in range(len(arr)):
    if arr[i] == first:
        temp += str(i)
        
for i in range(len(arr)):
    if arr[i] == second:
        temp += str(i)
        
temp = int(temp)
for i in range(len(arr)):
    if arr[i] == third:
        temp = temp * (10 ** i)
        
print(temp)
import sys
input = sys.stdin.readline


arr = set()
selfarr = []

def selfNumber(num:int):
    if num in arr:
        return    
    selfarr.append(num)
    while num <= 10000:
        total = num
        for digit in str(num):
            total += int(digit)
        arr.add(total)
        num = total
   
    
for i in range(1, 10001):
    selfNumber(i)


for num in selfarr:
    print(num)
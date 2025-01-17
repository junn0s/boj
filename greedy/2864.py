a, b = input().split()
tmp1 = list(a)
tmp2 = list(b)
tmp3 = list(a)
tmp4 = list(b)

for i in range(len(tmp1)):
    if tmp1[i] == '6':
        tmp1[i] = '5'
for i in range(len(tmp2)):
    if tmp2[i] == '6':
        tmp2[i] = '5'
        

for i in range(len(tmp3)):
    if tmp3[i] == '5':
        tmp3[i] = '6'
for i in range(len(tmp4)):
    if tmp4[i] == '5':
        tmp4[i] = '6'
        
res1 = 0
for i in range(len(tmp1)):
    res1 += int(tmp1[i]) * (10**(len(tmp1)-(i+1)))
for i in range(len(tmp2)):
    res1 += int(tmp2[i]) * (10**(len(tmp2)-(i+1)))
    
res2 = 0
for i in range(len(tmp3)):
    res2 += int(tmp3[i]) * (10**(len(tmp3)-(i+1)))
for i in range(len(tmp4)):
    res2 += int(tmp4[i]) * (10**(len(tmp4)-(i+1)))
    
print(res1, res2)


##################################################################################################

a, b = input().split()
min_sum = int(a.replace('6', '5')) + int(b.replace('6', '5'))
max_sum = int(a.replace('5', '6')) + int(b.replace('5', '6'))

print(min_sum, max_sum)
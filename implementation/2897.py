r, c = map(int, input().split())
parking = []
zero = 0
one = 0
two = 0
three = 0
four = 0
dot_count = 0
x_count = 0

for _ in range(r):
    temp = input().rstrip()
    parking.append(temp)

for i in range(r-1):
    for j in range(c-1):
        if parking[i][j] == "#" or parking[i][j+1] == "#" or \
            parking[i+1][j] == "#" or parking[i+1][j+1] == "#":
               continue
        if parking[i][j] == "." : dot_count += 1
        else : x_count += 1
        if parking[i][j+1] == "." : dot_count += 1
        else : x_count += 1
        if parking[i+1][j] == "." : dot_count += 1
        else : x_count += 1
        if parking[i+1][j+1] == "." : dot_count += 1
        else : x_count += 1
        
        if dot_count == 4 : zero += 1
        elif x_count == 1 : one += 1
        elif x_count == 2 : two += 1
        elif x_count == 3 : three += 1
        elif x_count == 4 : four += 1
        
        dot_count = 0
        x_count = 0
        
        
print(zero)
print(one)
print(two)
print(three)
print(four)
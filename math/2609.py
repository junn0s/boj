num1, num2 = map(int, input().split())

def loop(num1, num2):
    while num1 != num2:
        if num1 > num2:
            num1 = num1 - num2
        else:
            num2 = num2 - num1
    return num1

value = loop(num1, num2)
value2 = (num1 / value) * (num2 / value) * value

print(value)      
print(int(value2)) 

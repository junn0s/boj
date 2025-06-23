# 변수명

num, string = input().split()
if num == '2':
    tmp = string.split('_')
    tmp2 = ''
    for item in tmp:
        item = item[0].upper() + item[1:]
        tmp2 += item
    snake = string
    pascal = tmp2
    camel = tmp2[0].lower() + tmp2[1:]
elif num == '1':
    tmp = ''
    for i in range(len(string)):
        if string[i].isupper():
            tmp += '_' + string[i].lower()
        else:
            tmp += string[i]
    snake = tmp
    camel = string
    pascal = string[0].upper() + string[1:]
else:
    tmp = ''
    tmp += string[0].lower()
    for i in range(1, len(string)):
        if string[i].isupper():
            tmp += '_' + string[i].lower()
        else:
            tmp += string[i]
    snake = tmp
    pascal = string
    camel = string[0].lower() + string[1:]

print(camel)
print(snake)
print(pascal)
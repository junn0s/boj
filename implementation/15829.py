# hashing
# 입력 : 영문 소문자 1~26
# 모두 합한 후 1234567891로 나눠 줌
# 개선 : 각 항마다 고유 계수 부여
# 31의 0승부터 n승까지 곱

Mod = 1234567891

def dictionary(string:str):
    a = dict()
    for i in range(1, 27):
        a[string[i-1]] = i
    return a

def hash(string:str):
    i = 0
    arr = list()
    dict = dictionary("abcdefghijklmnopqrstuvwxyz")
    for item in string:
        item = dict[item]
        temp = int(item) * (31**i) % Mod
        arr.append(temp)
        i += 1
    
    res = sum(arr) % Mod
    return res



n = int(input())
string = input().rstrip()

print(hash(string))
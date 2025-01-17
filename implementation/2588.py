import sys
input = sys.stdin.readline

num1 = int(input())
num2 = int(input())

temp = list(str(num2))
print(num1 * int(temp[2]))
print(num1 * int(temp[1]))
print(num1 * int(temp[0]))
print(num1 * num2)
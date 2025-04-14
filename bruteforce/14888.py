# 연산자 끼워넣기
from itertools import permutations

def calculate(numbers, operators):
    result = numbers[0]
    for i in range(1, len(numbers)):
        op = operators[i - 1]
        num = numbers[i]
        if op == '+':
            result += num
        elif op == '-':
            result -= num
        elif op == '*':
            result *= num
        elif op == '/':
            if result < 0:
                result = -(-result // num)
            else:
                result = result // num
    return result

N = int(input())
numbers = list(map(int, input().split()))
plus, minus, multiply, divide = map(int, input().split())

operators = ['+'] * plus + ['-'] * minus + ['*'] * multiply + ['/'] * divide

unique_permutations = set(permutations(operators))

max_result = -float('inf')
min_result = float('inf')

for op_seq in unique_permutations:
    res = calculate(numbers, op_seq)
    max_result = max(max_result, res)
    min_result = min(min_result, res)

print(max_result)
print(min_result)
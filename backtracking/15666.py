# n과 m 12

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
numbers = set(map(int, input().split()))
numbers = sorted(numbers)

result = []

def backtrack(depth):
    if depth == M:
        print(*result)
        return
    
    for num in numbers:
        if result and result[-1] > num:
            continue
        result.append(num)
        backtrack(depth+1)
        result.pop()

backtrack(0)
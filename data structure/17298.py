import sys
input = sys.stdin.readline

def find_next_greater_elements(n, arr):
    nge = [-1] * n  
    stack = [] 
    for i in range(n):
        while stack and arr[stack[-1]] < arr[i]:
            idx = stack.pop()
            nge[idx] = arr[i]
        stack.append(i)

    return nge

N = int(input().strip())
A = list(map(int, input().strip().split()))

result = find_next_greater_elements(N, A)

print(' '.join(map(str, result)))

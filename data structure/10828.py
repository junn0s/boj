import sys
input = sys.stdin.readline

N = int(input())
stack = []

for _ in range(N):
    var = input().rstrip().split()
    if var[0] == 'push':
        stack.append(var[1])
    elif var[0] == 'pop':
        if stack:
            output = stack.pop()
            print(output)
        else:
            print(-1)
    elif var[0] == 'empty':
        if stack:
            print(0)
        else:
            print(1)
    elif var[0] == 'size':
        print(len(stack))
    elif var[0] == 'top':
        if stack:
            output = stack.pop()
            print(output)
            stack.append(output)
        else:
            print(-1)

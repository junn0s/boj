import sys
input = sys.stdin.readline

N = int(input())
queue = []

for _ in range(N):
    var = input().rstrip().split()
    if var[0] == 'push':
        queue.append(var[1])
    elif var[0] == 'pop':
        if queue:
            output = queue.pop(0)
            print(output)
        else:
            print(-1)
    elif var[0] == 'empty':
        if queue:
            print(0)
        else:
            print(1)
    elif var[0] == 'size':
        print(len(queue))
    elif var[0] == 'front':
        if queue:
            output = queue.pop(0)
            print(output)
            queue.insert(0,output)
        else:
            print(-1)
    elif var[0] == 'back':
        if queue:
            output = queue.pop()
            print(output)
            queue.append(output)
        else:
            print(-1)
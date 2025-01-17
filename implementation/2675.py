T = int(input())

for _ in range(T):
    R, S = input().split()
    arr = ''
    for char in S:
        string = char * int(R)
        arr += string
    print(arr)

T = int(input())

for _ in range(T):
    R, S = input().split()
    arr = ''
    for char in S:
        string = char * int(R)
        arr += string
    print(arr)




################################################################




T = int(input())
for _ in range(T):
    r, s = input().split()
    string = ''
    for char in s:
        string += char * int(r)
    print(string)
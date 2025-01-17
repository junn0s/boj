import sys
input = sys.stdin.readline


while True:
    A, B, C = map(int, input().rstrip().split())
    if A == 0 and B == 0 and C == 0:
        break
    else:
        temp = list()
        temp.append(A)
        temp.append(B)
        temp.append(C)
        temp.sort()
        if (temp[2]) ** 2 == (temp[0]) ** 2 + (temp[1]) ** 2:
            print("right")
        else:
            print("wrong")


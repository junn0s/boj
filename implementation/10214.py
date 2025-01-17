import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    y = 0
    k = 0
    for _ in range(9):
        ty, tk = map(int, input().split())
        y += ty
        k += tk
    if y > k:
        print("Yonsei")
    elif y < k:
        print("Korea")
    else:
        print("Draw")
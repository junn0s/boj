n = int(input())
arr = ["@@@@@", "@   @", "@   @", "@   @", "@@@@@"]


for i in range(5):
    for _ in range(n):
        for j in range(5):
            for _ in range(n):
                print(arr[i][j], end="")
        print()
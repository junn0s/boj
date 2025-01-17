n = int(input())
for i in range(n):
    arr = list(map(int, input().split()))
    arr.sort()
    if (arr[0])**2 + (arr[1])**2 == (arr[2])**2:
        print("Scenario #%d:" % (i+1))
        print("yes")
        print()
    else:
        print("Scenario #%d:" % (i+1))
        print("no")
        print()
    
def prime_list(m, n):
    arr = [True] * (n+1)
    arr[0] = arr[1] = False

    num = int(n ** 0.5)
    for i in range(2, num + 1):
        if arr[i] == True:           
            for j in range(2*i, n+1, i): 
                arr[j] = False

    return [i for i in range(m, n+1) if arr[i] == True]



m, n = map(int, input().split())
list = prime_list(m, n)
for item in list:
    print(item)
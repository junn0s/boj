# 소수
# 에라토스테네스 체 사용

def prime_list(m, n):
    arr = [True] * (n+1)
    arr[0] = arr[1] = False

    num = int(n ** 0.5)
    for i in range(2, num + 1):
        if arr[i] == True:           
            for j in range(2*i, n+1, i): 
                arr[j] = False

    return [i for i in range(m, n+1) if arr[i] == True]

m = int(input())
n = int(input())
list = prime_list(m, n)
res = sum(list)

if res == 0:
    print(-1)
else:
    print(res)
    print(min(list))
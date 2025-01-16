def coin(n:int):
    if n == 1 or n == 3:
        return -1
    five = n // 5
    for i in range(five, -1, -1):
        rest = n - (i * 5)
        if rest % 2 == 0 or rest == 0:
            two = rest // 2
            res = i + two
            break
    return res


n = int(input())
print(coin(n))
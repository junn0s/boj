def calc_number(val):
    result = val
    while val > 0:
        result += val % 10
        val //= 10
    return result


N = int(input())

result = 0
for curt in range(N // 10, N):
    if calc_number(curt) == N:
        result = curt
        break

print(result)
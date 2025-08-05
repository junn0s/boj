# 수 이어 쓰기

'''
1~9 까지 1 -> 9개..
10~99 까지 2 -> 90개
100~999 까지 3 -> 900개
1000~9999 까지 4 -> 9000개
10000~99999까지 5 -> 90000개..
'''

n = str(input().rstrip())
length = len(n)
total = 0
for i in range(1, length):
    total += 9 * 10**(i-1) * i
total += (int(n) - 10**(length-1) + 1) * length
print(total)
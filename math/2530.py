a, b, c = map(int, input().split())
d = int(input())

hour = d // 3600
minute = (d - (hour * 3600)) // 60
second = d % 60

res_second = (c + second) % 60
minute2 = (c + second) // 60
res_minute = (b + minute + minute2) % 60
hour2 = (b + minute + minute2) // 60
res_hour = (a + hour + hour2) % 24

print(res_hour, res_minute, res_second)
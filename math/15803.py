x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())
res = 0 #where
dx = x1 - x2
dy = y1 - y2
if dx == 0:
    if x3 == x1:
        res = 0
    else:
        res = 1
elif dy == 0:
    if y3 == y1:
        res = 0
    else:
        res = 1
else:
    if dy * (x3 - x1) == dx * (y3 - y1):
        res = 0
    else:
        res = 1
        
if res == 0:
    print("WHERE IS MY CHICKEN?")
else:
    print("WINNER WINNER CHICKEN DINNER!")
a, b, c = map(int, input().split())
two = 0
three = 0

if a == b:
    two = a
if a == c:
    two = a
if b == c:
    two = b
if a == b == c:
    three = a
    
if three != 0:
    print(10000 + (three * 1000))
elif two != 0:
    print(1000 + (two * 100))
else:
    print(max(a,b,c) * 100)
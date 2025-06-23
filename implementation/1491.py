import sys
input = sys.stdin.readline

n, m = map(int, input().split())
left, right = 0, n - 1
bottom, top = 0, m - 1

x, y = 0, 0
last_x, last_y = 0, 0

while True:
    for x in range(left, right + 1):
        last_x, last_y = x, y
    bottom += 1
    if bottom > top:
        break

    for y in range(bottom, top + 1):
        last_x, last_y = x, y
    right -= 1
    if left > right:
        break

    for x in range(right, left - 1, -1):
        last_x, last_y = x, y
    top -= 1
    if bottom > top:
        break

    for y in range(top, bottom - 1, -1):
        last_x, last_y = x, y
    left += 1
    if left > right:
        break

print(last_x, last_y)
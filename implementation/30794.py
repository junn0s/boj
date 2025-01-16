lv, state = input().split()
if state == "miss":
    print(0)
elif state == "bad":
    print(200 * int(lv))
elif state == "cool":
    print(400 * int(lv))
elif state == "great":
    print(600 * int(lv))
else:
    print(1000 * int(lv))
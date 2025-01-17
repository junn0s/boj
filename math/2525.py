hour, minute = map(int, input().split())
needtime = int(input())

def time(hour, minute, needtime):
    minute += needtime
    if minute >= 60:
        hour += minute // 60
        minute %= 60
        if hour >= 24:
            hour %= 24
    return (hour, minute)

hour, minute = time(hour, minute, needtime)
print(hour, minute)
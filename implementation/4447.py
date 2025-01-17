import sys
input = sys.stdin.readline

n = int(input())
for _ in range(n):
    name = input().rstrip()
    good = 0
    bad = 0
    res = ""
    for alpa in name:
        if alpa == "g" or alpa == "G":
            good += 1
        elif alpa == "b" or alpa == "B":
            bad += 1
    
    if good == bad:
        res = "NEUTRAL"
    elif good > bad:
        res = "GOOD"
    else:
        res = "A BADDY"
        
    print("%s is %s" % (name, res))
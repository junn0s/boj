T = int(input())

for i in range(1, T+1):
    score = int(input())
    if score <= 25:
        print("Case #%d: World Finals" % i)
    elif score <= 1000:
        print("Case #%d: Round 3" % i)
    elif score <= 4500:
        print("Case #%d: Round 2" % i)
    else:
        print("Case #%d: Round 1" % i)
        

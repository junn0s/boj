# 7종 경기

t = int(input())
for _ in range(t):
    res = []
    a, b, c, d, e, f, g = map(int, input().split())
    res.append(int(9.23076 * (26.7 - a)**(1.835)))
    res.append(int(1.84523 * (b - 75)**(1.348)))
    res.append(int(56.0211 * (c - 1.5)**(1.05)))
    res.append(int(4.99087 * (42.5 - d)**(1.81)))
    res.append(int(0.188807 * (e - 210)**(1.41)))
    res.append(int(15.9803 * (f - 3.8)**(1.04)))
    res.append(int(0.11193 * (254 - g)**(1.88)))
    print(sum(res))
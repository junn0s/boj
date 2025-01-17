N = int(input())
score = list(map(int, input().split()))

max = max(score)
new_score = []
for item in score:
    new = (item / max) * 100
    new_score.append(new)

sum = 0    
for item in new_score:
    sum += item

sum = sum / N
print(sum)
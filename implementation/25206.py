import sys
input = sys.stdin.readline

arr = list()
for _ in range(20):
    name, score, grade = input().split()
    if grade == 'P':
        continue
    elif grade == 'A+':
        grade = 4.5
    elif grade == 'A0':
        grade = 4.0
    elif grade == 'B+':
        grade = 3.5
    elif grade == 'B0':
        grade = 3.0
    elif grade == 'C+':
        grade = 2.5
    elif grade == 'C0':
        grade = 2.0
    elif grade == 'D+':
        grade = 1.5
    elif grade == 'D0':
        grade = 1.0
    elif grade == 'F':
        grade = 0.0
    arr.append((name, float(score), grade))

sum = 0
count = 0  
for i in range(len(arr)):
    sum += arr[i][1] * arr[i][2]
    count += arr[i][1]
total = sum / count
print(total)
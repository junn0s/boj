import sys
input = sys.stdin.readline

def boy(num, switch_num, switch):
    i = 1
    while num * i <= switch_num:
        index = num * i - 1
        if switch[index] == 0:
            switch[index] = 1
        else:
            switch[index] = 0
        i += 1 
    return switch

def girl(num, switch_num, switch):
    i = 1
    left_num = num-1
    right_num = num+1
    if switch[num-1] == 0:
        switch[num-1] = 1
    else:
        switch[num-1] = 0
        
    while left_num >= 1 and right_num <= switch_num:
        if switch[left_num-1] == switch[right_num-1]:
            if switch[left_num-1] == 0:
                switch[left_num-1] = 1
                switch[right_num-1] = 1
            else:
                switch[left_num-1] = 0
                switch[right_num-1] = 0
            i += 1
            left_num = num-i
            right_num = num+i
        else:
            break

    return switch

switch_num = int(input())
switch = list(map(int, input().split()))
student_num = int(input())

for _ in range(student_num):
    gender, num = map(int, input().split())
    if gender == 1:
        switch = boy(num, switch_num, switch)
    elif gender == 2:
        switch = girl(num, switch_num, switch)
        
        
for i in range(0, len(switch), 20):
    print(" ".join(map(str, switch[i:i + 20])))

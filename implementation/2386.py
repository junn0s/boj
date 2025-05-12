# 도비의 영어 공부

import sys
input = sys.stdin.readline

while True:
    sentence = input()
    char = sentence[0]
    count = -1
    if char == '#':
        break
    sentence = sentence.lower()
    for item in sentence:
        if item == char:
            count += 1
    print(char, count)
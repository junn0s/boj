import sys
input = sys.stdin.readline

temp = input().rstrip()
word = list(temp.lower())
wordlist = dict()

for i in range(0, len(word)):
    if word[i] == '@':
        continue
    temp = word[i]
    count = 1
    for j in range(i+1, len(word)):
        if word[j] == temp:
            count += 1
            #word = word[:j] + '@' + word[j+1:]
            word[j] = '@'
    
    if temp in wordlist:
        wordlist[temp] += count
    else:
        wordlist[temp] = count
        
wordlist = sorted(wordlist.items(), key=lambda x:x[1], reverse=True)
if len(wordlist) > 1 and wordlist[0][1] == wordlist[1][1]:
    print("?")
else:
    print(wordlist[0][0].upper())
    
    
    
    
'''
from collections import Counter
import sys

input = sys.stdin.readline

word = input().rstrip().lower()
counter = Counter(word)

# 가장 많은 빈도 수 찾기
max_count = max(counter.values())

# 빈도 수가 같은 알파벳 확인
most_common = [k for k, v in counter.items() if v == max_count]

if len(most_common) > 1:
    print("?")
else:
    print(most_common[0].upper())
'''

import sys
input = sys.stdin.readline

word = input().rstrip().lower()
wordlist = {}  # 빈 딕셔너리 생성

# 단일 반복문으로 문자 개수 세기
for char in word:
    if char in wordlist:
        wordlist[char] += 1
    else:
        wordlist[char] = 1

# 최대 빈도와 해당 문자를 찾기
max_count = 0
max_chars = []

for key in wordlist:
    if wordlist[key] > max_count:
        max_count = wordlist[key]
        max_chars = [key]
    elif wordlist[key] == max_count:
        max_chars.append(key)

# 결과 출력
if len(max_chars) > 1:
    print("?")
else:
    print(max_chars[0].upper())

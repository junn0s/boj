import sys
input = sys.stdin.readline

wordlist = input().rstrip()
numlist = list()
for word in wordlist:
    if word == 'A' or word == 'B' or word == 'C':
        numlist.append(3)
    elif word == 'D' or word == 'E' or word == 'F':
        numlist.append(4)
    elif word == 'G' or word == 'H' or word == 'I':
        numlist.append(5)
    elif word == 'J' or word == 'K' or word == 'L':
        numlist.append(6)
    elif word == 'M' or word == 'N' or word == 'O':
        numlist.append(7)
    elif word == 'P' or word == 'Q' or word == 'R' or word == 'S':
        numlist.append(8)
    elif word == 'T' or word == 'U' or word == 'V':
        numlist.append(9)
    elif word == 'W' or word == 'X' or word == 'Y' or word == 'Z':
        numlist.append(10)
        
print(sum(numlist))
count = [-1] * 26
alphabet = 'abcdefghijklmnopqrstuvwxyz'
S = input()

for i, char in enumerate(S):
    index = ord(char) - ord('a')
    if count[index] == -1:
        count[index] = i

print(' '.join(map(str, count)))
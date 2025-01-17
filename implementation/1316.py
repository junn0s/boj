import sys
input = sys.stdin.readline

def group(word:str):
    arr = list()
    arr.append(word[0])
    for i in range(len(word)-1):
        if word[i] == word[i+1]:
            continue
        else:
            if word[i+1] in arr:
                return False
            else:
                arr.append(word[i+1])
    return True

N = int(input().rstrip())
count = 0
for i in range(N):
    word = input().rstrip()
    if group(word) == True:
        count += 1
print(count)
n = int(input())
word_list = []
for _ in range(n):
    word = str(input().rstrip())
    word_list.append(word)

word_list = set(word_list)
word_list = list(word_list)
word_list.sort(key=lambda x:len(x))

n = len(word_list)
cnt = 0
for i in range(n):
    now_word = word_list[i]
    for j in range(i+1, n):
        state = True
        next_word = word_list[j]
        for k in range(len(now_word)):
            if now_word[k] == next_word[k]:
                continue
            else:
                state = False
                break
        if state:
            cnt += 1
            break

print(n - cnt)
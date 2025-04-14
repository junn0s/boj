# 단어 퍼즐

index = 1
while True:
    res_word = input()
    tem_word = input()
    if res_word == 'END' and tem_word == 'END':
        break
    if sorted(res_word) == sorted(tem_word):
        flag = 'same'
    else:
        flag = 'different'
    print(f"Case {index}: {flag}")
    index += 1
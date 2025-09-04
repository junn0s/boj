# 2021 카카오 채용연계형 인턴십

# "23four5six7" → 234567  

def solution(s:str):
    num_word = {'zero':'0', 'one':'1', 'two':'2', 'three':'3', 'four':'4', 'five':'5', 'six':'6',
                'seven':'7', 'eight':'8', 'nine':'9'}
    answer = ''
    tmp = ''
    for i in range(len(s)):
        if s[i].isdigit() == True:
            answer += s[i]
        else:
            tmp += s[i]
            if tmp in num_word:
                answer += num_word[tmp]
                tmp = ''
        
    return int(answer)
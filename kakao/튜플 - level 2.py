# 2019 카카오 겨울 인턴십

def solution(s:str):
    s = s[1:-1]
    numlist = list()
    tmp = []
    tmpnum = ''
    for num in s:
        if num == '{': 
            continue
        elif num == '}': 
            if tmpnum == '':
                continue
            tmp.append(tmpnum)
            numlist.append(tmp)
            tmp = []
            tmpnum = ''
        else:
            if num == ',':
                if tmpnum == '':
                    continue
                tmp.append(tmpnum)
                tmpnum = ''
            else:
                tmpnum += num
    
    numlist.sort(key=len)
    answer = []

    for tmplist in numlist:
        for num in tmplist:
            if num:
                num = int(num)
            else:
                continue
            if answer and num in answer:
                continue
            else:
                answer.append(num)

    return answer
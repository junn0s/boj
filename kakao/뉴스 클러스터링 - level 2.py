# 2018 kakao blind 채용

from collections import Counter

def solution(str1:str, str2:str):
    alpa = 'abcdefghijklmnopqrstuvwxyz'

    str1 = str1.lower()
    str2 = str2.lower()

    first = list()
    second = list()

    for i in range(len(str1)-1):
        if str1[i] in alpa and str1[i+1] in alpa:
            tmp = str1[i] + str1[i+1]
            first.append(tmp)

    for i in range(len(str2)-1):
        if str2[i] in alpa and str2[i+1] in alpa:
            tmp = str2[i] + str2[i+1]
            second.append(tmp)

    first.sort()
    second.sort()

    if len(second) < len(first):
        second, first = first, second


    a = Counter(first)
    b = Counter(second)
    lena = sum((a & b).values())
    lenb = sum((a | b).values())
    if lenb == 0:
        return 65536
    answer = int(lena / lenb * 65536)
    return answer
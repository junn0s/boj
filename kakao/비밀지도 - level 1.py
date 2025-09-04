# 2018 kakao blind 채용

def solution(n:int, arr1:list, arr2:list):
    answer = []

    for i in range(n):
        tmp = bin(arr1[i] | arr2[i])[2:].zfill(n)
        answer.append(tmp.replace('0', ' ').replace('1', '#'))    

    return answer
def solution(dartResult):
    num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
    bonus = {'S':1, 'D':2, 'T':3}
    option = {'*':2, '#':-1}
    num_arr = []
    bonus_arr = []
    check = []
    option_arr = []
    skip = False
    for i in range(len(dartResult)):
        if skip:
            skip = False
            continue
        if dartResult[i] == '1' and i+1 < len(dartResult) and dartResult[i+1] == '0':
            tmp = 10
            num_arr.append(tmp)
            skip = True
        elif dartResult[i] in num:
            tmp = int(dartResult[i])
            num_arr.append(tmp)
    
    for i in range(len(dartResult)):
        if dartResult[i] in bonus.keys():
            bonus_arr.append(bonus[dartResult[i]])
            check.append(dartResult[i])
        
    for i in range(len(dartResult)):
        if dartResult[i] in check:
            if i+1 < len(dartResult) and dartResult[i+1] in option.keys():
                option_arr.append(option[dartResult[i+1]])
            else:
                option_arr.append(1)
    
    for i in range(3):
        if option_arr[i] == 2 and i !=0:
            option_arr[i-1] *= 2
            
    res = 0   
    for i in range(3):    
        res += (num_arr[i] ** bonus_arr[i] ) * option_arr[i]
        
    answer = res
    return answer
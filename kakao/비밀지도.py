def solution(n, arr1, arr2):
    bin_arr1 = []
    for j in range(n):
        tmp = ''
        i = n
        while i > 0:
            if 2**(i-1) <= arr1[j] < 2**i:
                tmp += '1'
                arr1[j] -= 2**(i-1)
            else:
                tmp += '0'
            i -= 1
        bin_arr1.append(tmp)

    bin_arr2 = []
    for j in range(n):
        tmp = ''
        i = n
        while i > 0:
            if 2**(i-1) <= arr2[j] < 2**i:
                tmp += '1'
                arr2[j] -= 2**(i-1)
            else:
                tmp += '0'
            i -= 1
        bin_arr2.append(tmp)
    
    res_arr = []  
    for i in range(n):
        tmp = ''
        for j in range(n):
            if bin_arr1[i][j] == '1' or bin_arr2[i][j] == '1':
                tmp += '#'
            else:
                tmp += ' '
        res_arr.append(tmp)
        
    answer = res_arr
    return answer



n = 5
arr1 = [9, 20, 28, 18, 11]
arr2 = [30, 1, 21, 17, 28]
print(solution(n, arr1, arr2))
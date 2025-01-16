def solution(friends, gifts):
    arr = [[0 for _ in range(len(friends))] for _ in range(len(friends))]
    for j in range(len(friends)):
        for i in range(len(gifts)):
            a, b = gifts[i].split()
            if a == friends[j]:
                for k in range(len(friends)):
                    if friends[k] == b:
                        arr[j][k] += 1
    arr2 = []                  
    for i in range(len(friends)):
        gift = 0
        for j in range(len(friends)):
            gift += arr[i][j]
            gift -= arr[j][i]
        arr2.append(gift)
    
    res = [0 for _ in range(len(friends))]
    for i in range(len(friends)):
        for j in range(i+1, len(friends)):
            if j < len(friends):
                if arr[i][j] > arr[j][i]:
                    res[i] += 1
                elif arr[i][j] < arr[j][i]:
                    res[j] += 1
                elif arr[i][j] == arr[j][i] or (arr[i][j] == 0 and arr[j][i] == 0):
                    if arr2[i] > arr2[j] :
                        res[i] += 1
                    elif arr2[i] < arr2[j]:
                        res[j] += 1
                                        
    return max(res)



friends = ["a", "b", "c"]
gifts = ["a b", "b a", "c a", "a c", "a c", "c a"]
print(solution(friends, gifts))
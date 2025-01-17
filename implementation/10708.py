n = int(input())
m = int(input())
name_Paper = dict()
res = dict()
for i in range(1, n+1):
    res[i] = 0
target = list(map(int, input().split()))
for i in range(m):
    temp = list(map(int, input().split()))
    for j in range(1, n+1):
        name_Paper[j] = temp[j-1]
    target_name = target[i]
    
    count = 0
    for item in name_Paper.values():
        if item != target_name:
            count += 1
    res[target_name] += count + 1
    
    
    for name, write in name_Paper.items():
        if name != target_name and write == target_name:
            res[name] += 1
                
                
for item in res.values():
    print(item)



######################################################################################



n = int(input())
m = int(input())
targets = list(map(int, input().split()))

# 이름(1~n)에 대한 결과를 저장할 리스트
# 인덱스를 1부터 사용하기 위해 n+1 길이로 만듦 (0번 인덱스 미사용)
res = [0] * (n + 1)

for i in range(m):
    temp = list(map(int, input().split()))
    target_name = targets[i]

    # temp 중 target_name이 몇 번 나왔는지 계산
    target_count = sum(1 for w in temp if w == target_name)
    # target_name이 아닌 다른 값의 개수
    diff_count = n - target_count

    # target_name인 사람의 결과에 (diff_count + 1) 추가
    res[target_name] += diff_count + 1

    # target_name을 쓴 사람들에게 각각 +1
    for name in range(1, n + 1):
        if name != target_name and temp[name - 1] == target_name:
            res[name] += 1

for item in res[1:]:
    print(item)
    
###################################################################################

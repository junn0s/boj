# 멀티탭 스케줄링


# 멀티탭 구멍이 꽉 찼는데 새 기기를 꽂아야 하면:
# 	1.	이미 꽂혀 있으면 아무것도 안 함
# 	2.	빈 구멍이 있으면 그냥 꽂음
# 	3.	꽉 찼으면 현재 꽂힌 기기들 중에서
# 	•	앞으로 다시 안 나오는 기기가 있으면 그걸 뽑음(가장 우선)
# 	•	모두 다시 나온다면, 가장 “나중에” 다시 쓰이는 기기를 뽑음

# 현재 멀티탭에 꽂힌 각 기기 x에 대해,
# 	•	현재 인덱스 i 이후 구간에서 x가 처음 등장하는 위치를 찾음
# 	•	없으면 “무한대(매우 큰 값)”로 처리
# 	•	그 위치가 가장 큰(=가장 늦게 다시 등장) 기기를 뽑기


import sys
input = sys.stdin.readline

n, k = map(int, input().split())
count_arr = list(map(int, input().split()))
multitap = []
result = 0

for i in range(k):
    if count_arr[i] in multitap:
        continue
    elif len(multitap) < n:
        multitap.append(count_arr[i])
    else:
        last_index = []
        for j in range(len(multitap)):
            x = multitap[j]
            index = 10000
            for m in range(i+1, k):
                if count_arr[m] == x:
                    index = m
                    break
            last_index.append([index, x])
        last_index.sort(reverse=True)
        pop = last_index[0][1]
        multitap.remove(pop)
        multitap.append(count_arr[i])
        result += 1

print(result)


            
                




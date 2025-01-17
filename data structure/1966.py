import sys
from collections import deque
input = sys.stdin.readline
  
    
def priority_print(arr:deque, m:int):
    count = 0
    while True:
        for item in arr:
            if arr[0] < item:
                temp = arr.popleft()
                arr.append(temp)
                if m == 0:
                    m = len(arr) - 1
                else:
                    m -= 1
                break
        else:
            arr.popleft()
            count += 1
            if m == 0:
                return count
            else:
                m -= 1
                
                
t = int(input())
for _ in range(t):
    n, m = map(int, input().rstrip().split())
    arr = deque(map(int, input().rstrip().split()))
    print(priority_print(arr, m))
    
    
    
################## 아래는 chat gpt 코드 ##################

import sys
from collections import deque

input = sys.stdin.readline

def priority_print(arr: deque, m: int) -> int:
    count = 0
    while arr:
        max_priority = max(arr)  # 현재 큐에서 가장 높은 우선순위 찾기
        current = arr.popleft()  # 큐의 맨 앞 문서 꺼내기
        m -= 1  # 목표 문서 위치 업데이트

        if current == max_priority:
            count += 1  # 인쇄된 문서 수 증가
            if m < 0:  # 목표 문서가 인쇄되면 종료
                return count
        else:
            arr.append(current)  # 우선순위가 낮으면 뒤로 보내기
            if m < 0:  # 목표 문서가 큐의 끝으로 이동
                m = len(arr) - 1

    return count

# 입력 및 실행
t = int(input())
for _ in range(t):
    n, m = map(int, input().rstrip().split())
    arr = deque(map(int, input().rstrip().split()))
    print(priority_print(arr, m))

#########################################################
# 2018 kakao blind 채용

from collections import deque

def solution(cacheSize, cities):
    q = deque()
    if cacheSize == 0:
        return len(cities) * 5

    answer = 0
    for city in cities:
        city = city.lower()
        if city in q:
            answer += 1
            q.remove(city)
            q.append(city)
        else:
            answer += 5
            if len(q) == cacheSize:
                q.popleft()
                q.append(city)
            else:
                q.append(city)


    return answer
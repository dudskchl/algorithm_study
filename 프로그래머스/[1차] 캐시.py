
from collections import deque


def solution(cacheSize, cities):
    total_time=0

    c_size=cacheSize #deque 사이즈
    q=deque()       #deque 자료형

    for i in range(len(cities)):   #대소문자 구별x
        cities[i]=cities[i].lower()

    
    for i in cities:
        if i in q:      #큐에 찾고자 하는 값이 있을 경우
            q.remove(i)     #가장 왼쪽?에 있는 i항목 삭제됨
            q.append(i)
            total_time+=1    #cache hit
        else:
            q.append(i)     #큐 오른쪽쪽에 삽입

            if len(q)>c_size:
                q.popleft()  #캐시사이즈보다 커지면 큐 왼쪽 원소 삭제
            total_time+=5    #cache miss
            
        
    return total_time

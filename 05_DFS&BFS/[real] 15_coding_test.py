import numpy as np
import random
from collections import deque

n = 4 #도시의 개수
m = 4 #도로의 개수
k = 2 #거리 정보
x = 1 #출발 도시의 정보

roads = [[1, 2], [1, 3], [2, 3], [2, 4]]
cities = []

for road in roads:
    temp = road
    for test in roads:
        if temp[1] == test[0]:
            cities.append(test[1])
            
for road in roads:
    for i, city in enumerate(cities):
        if [x, city] == road:
            cities.pop(i)

if len(cities) == 0:
    print(-1)
else:
    print(cities)


#정답코드
from collections import deque

#도시의 개수, 도로의 개수, 거리 정보, 출발 도시 정보
n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n+1)]

#모든 도로 정보 입력받기
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

#모든 도시에 대한 최단 거리 초기화
distance = [-1] * (n+1)
distance[x] = 0 #출발 도시까지의 거리는 0으로 설정

#너비 우선 탐색(BFS) 수행
q = deque([x])
while q:
    now = q.popleft()
    #현재 도시에서 이동할 수 있는 모든 도시를 확인
    for next_node in graph[now]:
        #아직 방문하지 않은 도시라면
        if distance[next_node] == -1:
            #최단 거리 갱신
            distance[next_node] = distance[now] + 1
            q.append(next_node)

#최단 거리가 K인 모든 도시의 번호를 오름차순으로 출력
check = False
for i in range(1, n + 1):
    if distance[i] == k:
        print(i)
        check = True

#만약 최단 거리가 K인 도시가 없다면, -1 출력
if check == False:
    print(-1)
    
    
    
    
    
    
    
    
    
    
    
    
    

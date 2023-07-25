#정답코드
from collections import deque
import numpy as np
import random

n = 3 #시험관 크기
k = 3 #바이러스 종류

s = 1
x = 2
y = 2


#연구소 정보
data = [[1,0,2], [0,0,0], [3,0,0]]

for i in range(n):
    for j in range(n):
        data[i][j]

#방향 정하기[상, 하, 좌, 우]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def virus(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]        
        
        # 상, 하, 좌, 우 중에서 바이러스가 퍼질 수 있는 경우
        if nx >= 0 and nx < n and ny >= 0 and ny < n:                
            if data[nx][ny] == 0:
                #해당 위치에 바이러스 배치하고, 다시 재귀적으로 수행
                data[nx][ny] = data[x][y]
                # virus(nx, ny)
    
virus_start = []
empty = []
#바이러스 사이즈가 작은것 부터 채워 나가기
for p in range(1, k+1):
    for i in range(n):
        for j in range(n):
            if data[i][j] == p:
                virus_start.append([i, j])
            if data[i][j] == 0:
                empty.append([i, j])

#채워 나가야할 부분들 좌표 저장하기
result = []
for value in empty:
    if value not in result:
        result.append(value)
    
#가장 작은 바이러스 숫자 부터 옆으로 퍼져 나가기
def simul():
    for i in range(s):
        for time in virus_start:
            virus(time[0], time[1])
    
    print(data[x-1][y-1])
                    
simul()

#정답 코드
from collections import deque

n, k = map(int, input().split())

graph = [] # 전체 보드 정보를 담는 리스트
data = [] # 바이러스에 대한 정보를 담는 리스트

for i in range(n):
    #보드 정보를 한 줄 단위로 입력
    graph.append(list(map(int, input().split())))
    for j in range(n):
        #해당 위치에 바이러스가 존재하는 경우
        if graph[i][j] != 0:
            #(바이러스 종류, 시간, 위치 X, 위치 Y) 삽입
            data.append((graph[i][j], 0, i, j))

#정렬 이후에 큐로 옮기기(낮은 번호의 바이러스가 먼저 증식하므로)
data.sort()
q = deque(data)

target_s, target_x, target_y = map(int, input().split())

#바이러스가 퍼져나갈 수 있는 4가지 위치
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

#너비 우선 탐색(BFS) 진행
while q:
    virus, s, x, y = q.popleft()
    #정확히 s초가 지나거나, 큐가 빌 때까지 반복
    if s == target_s:
        break

    #현재 노드에서 주변 4가지 위치를 각각 확인
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        #해당 위치로 이동할 수 있는 경우
        if <= nx and nx < n and 0 <= ny and ny < n :
            #아직 방문하지 않은 위치라면, 그 위치에 바이러스 넣기
            if graph[nx][ny] == 0:
                graph[nx][ny] = virus
                q.append((virus, s + 1, nx, ny))

print(graph[target_X - 1][target_y - 1])
                
                
                
                
                
                
                

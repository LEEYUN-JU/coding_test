#정답코드
from collections import deque
import numpy as np
import random

n = 3 #시험관 크기
k = 3 #바이러스 종류

temp = [[0] * n for _ in range(n)] #벽을 설치한 뒤의 맵 리스트

#연구소 정보
data = [[1,0,2], [0,0,0], [3,0,0], [2,3,2]]

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
        if nx >= 0 and nx < n and ny >= 0 and ny < m:
            if temp[nx][ny] == 0:
                #해당 위치에 바이러스 배치하고, 다시 재귀적으로 수행
                temp[nx][ny] = 2
                virus(nx, ny)
    
#현재 맵에서 안전 영역의 크기 계산하는 메서드
def get_score():
    score = 0
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 0:
                score += 1
                
    return score

#깊이 우선 탐색(DFS)을 이용해 울타리를 설치하면서, 매번 안전 영역의 크기 계산
def dfs(count):
    global result
    #울타리가 3개 설치된 경우
    if count == 3:
        for i in range(n):
            for j in range(m):
                temp[i][j] = data[i][j]
        
        #각 바이러스의 위치에서 전파 진행
        for i in range(n):
            for j in range(m):
                if temp[i][j] == 2:
                    virus(i, j)
                    
        #안전 영역의 최댓값 계산
        result = max(result, get_score())
        print(result)
        return
    
    #빈 공간에 울타리 설치
    for i in range(n):
        for j in range(m):
            if data[i][j] == 0:
                data[i][j] == 1
                count += 1
                dfs(count)
                data[i][j] == 0
                count -= 1
                
dfs(0)
print(result)           
                
                
                
                
                
                
                
                
                
                
                
                
                
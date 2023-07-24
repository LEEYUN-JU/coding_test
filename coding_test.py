import numpy as np
import random

n = np.random.randint(1, 1001)
m = np.random.randint(1, 1001)

maps = []

for i in range(0, n):
    temp = []
    for j in range(0, m):
        temp.append(np.random.randint(0, 2))
    
    maps.append(temp)

def dfs(x, y):
    # 주어진 범위를 벗어나는 경우에는 즉시 종료
    if x <= -1 or x >= n or y <= -1 or y >= m :
        return False
    
    # 현재 노드를 아직 방문하지 않았다면
    if maps[x][y] == 0:
        #해당 노드 방문 처리
        maps[x][y] = 1
        #상, 하, 좌, 우의 위치도 모두 재귀적으로 호출
        dfs(x, y - 1) #상
        dfs(x - 1, y) #좌
        dfs(x + 1, y) #우
        dfs(x, y + 1) #하
        return True
    
    return False

#모든 노드(위치)에 대하여 음료수 채우기
result = 0
for i in range(n):
    for j in range(m):
        #현재 위치에서 DFS수행
        if dfs(i, j) == True:
            result += 1
            
print(result) #정답 출력



    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
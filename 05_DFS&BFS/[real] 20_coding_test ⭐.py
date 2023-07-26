from collections import deque
import numpy as np
import random
from itertools import permutations, combinations

n = 5

#학교 정보
# H = 0, S = 1, T = 2, O = 3
data = [[0,1,0,0,2],[2,0,1,0,0],[0,0,0,0,0],[0,2,0,0,0],[0,0,2,0,0]]

#방향 정하기[상, 하, 좌, 우]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

temp = [[0] * n for _ in range(n)] #벽을 설치한 뒤의 맵 리스트           

def virus(x, y):    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]        
        
            
        # 상, 하, 좌, 우를 끝까지 살펴보기
        for j in range(n):
            
            if i == 0:
                nx = x + dx[i] - j
                
            if i == 1:
                nx = x + dx[i] + j
                
            if i == 2:
                ny = y + dx[i] - j
                
            if i == 3:
                ny = y + dx[i] + j
    
            
            if nx >= 0 and nx < n and ny >= 0 and ny < n:                
                if temp[nx][ny] == 1:
                    return False
        
                
check = 0

#깊이 우선 탐색(DFS)을 이용해 울타리를 설치하면서, 매번 안전 영역의 크기 계산
def dfs(count):  
    #울타리가 3개 설치된 경우
    if count == 3:
        for i in range(n):
            for j in range(n):
                temp[i][j] = data[i][j]
        
        #선생님이 학생을 확인 가능한지 확인
        for i in range(n):
            for j in range(n):
                if temp[i][j] == 2:
                    check = virus(i, j)

        #print(check)
        return check
        
    
    #빈 공간에 울타리 설치
    for i in range(n):
        for j in range(n):
            if data[i][j] == 0:
                data[i][j] = 3
                count += 1
                dfs(count)
                data[i][j] = 0
                count -= 1
            
                
dfs(0)

if check == True:
    print ("YES")
    
if check == False:
    print ("NO")


#정답 코드
from itertools import combinations

n = int(input()) #복도의 크기
board = [] #복도 정보(N x N)
teachers = [] #모든 선생님 위치 정보
spaces = [] #모든 빈 공간 위치 정보

for i in range(n):
    board.append(list(input().split()))
    for j in range(n):
        #선생님이 존재하는 위치 저장
        if board[i][j] == 'T':
            teachers.append((i, j))
            
        #장애물을 설치할 수 있는 (빈 공간) 위치 저장
        if board[i][j] == 'X':
            spaces.append((i, j))
            
#특정 방향으로 감시를 진행(학생 발견 :True, 학생 미발견 : False)
def watch(x, y, direction):
    #왼쪽 방향으로 감시
    if direction == 0:
        while y >= 0:
            if board[x][y] == 'S': #학생이 있는 경우
                return True
            if board[x][y] == 'O': #학생이 있는 경우
                return False
            y -= 1
            
    #오른쪽 방향으로 감시
    if direction == 1:
        while y < n:
            if board[x][y] == 'S': #학생이 있는 경우
                return True
            if board[x][y] == 'O': #학생이 있는 경우
                return False
            y += 1
            
    #위쪽 방향으로 감시
    if direction == 2:
        while x >= 0:
            if board[x][y] == 'S': #학생이 있는 경우
                return True
            if board[x][y] == 'O': #학생이 있는 경우
                return False
            x -= 1
            
    #아래쪽 방향으로 감시
    if direction == 3:
        while x < n:
            if board[x][y] == 'S': #학생이 있는 경우
                return True
            if board[x][y] == 'O': #학생이 있는 경우
                return False
            x += 1
            
    return False
        
#장애물 설치 이후에 , 한 명이라도 학생이 감지되는지 검사
def process():
    #모든 선생님의 위치를 하나씩 확인
    for x, y in teachers:
        #4가지 방향으로 학생을 감지할 수 있는지 확인
        for i in range(4):
            if watch(x, y, i):
                return True
        
        return False

    find = False #학생이 한 명도 감지되지 않도록 설치할 수 있는지의 여부

    #빈 공간에서 3개를 뽑는 모든 조합을 확인
    for data in combinations(spaces, 3):
        #장애물 설치해보기
        for x, y in data:
            board[x][y] = 'O'
            
        #학생이 한 명도 감지되지 않는 경우
        if not process():
            #원하는 경우를 발견한 것임
            find = True
            break
        #설치된 장애물을 다시 없애기
        for x, y in data:
            board[x][y] = 'X'
            
    if find:
        print('YES')
    else:
        print('NO')
    
                    
 





                
                
                

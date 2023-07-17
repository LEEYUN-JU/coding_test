import numpy as np

game_map_size = np.random.randint(2, 101)
apple = np.random.randint(0, 101)

snake_L = np.random.randint(1, 101) #방향 변환 횟수

snake_direction = [0,1,2,3] #0 북 #1 서 #2 남 #3 동

snake_record = []   #지나온 길
snake_goes = []     #가야할 방향 및 시긴

#뱀 회전 함수
def rotation(direction, current):
    if direction[1] == "L":
        current[0] += 1
        if current[0] == 4:
            current[0] = 0
            
    if direction[1] == "D":
        current[0] -= 1
        if current[0] == -1:
            current[0] = 3        
    
    return current

#맵 생성하기
game_map = [[0 for j in range(game_map_size)] for i in range(game_map_size)]
apple_rocation = []

for i in range(0, apple):
    apple_rocation.append([np.random.randint(1, game_map_size), np.random.randint(1, game_map_size)])
    
for i in range(0, snake_L):
    snake_goes.append([np.random.randint(1, 11), np.random.randint(0, 2)]) #0 == L, 1 == D

for i in range(0, len(snake_goes)):
    if snake_goes[i][1] == 0:
        snake_goes[i][1] = "L"
    if snake_goes[i][1] == 1:
        snake_goes[i][1] = "D"

#뱀의 초기 위치 설정하기
current = [3, [0,0]]
snake_length = 1
take_time = 1

end = 0

while True:
    if end == 1:
        break
    
    try:
        update = snake_goes.pop(0)
        
    except:
        print(take_time)
    
    current = rotation(update, current)
    
    for i in range(0, update[0]):
        #북쪽
        
        if current[0] == 0:
            current[1][0] -= 1
            
        if current[0] == 1:
            current[1][1] -= 1
            
        if current[0] == 2:
            current[1][0] += 1
            
        if current[0] == 3:
            current[1][1] += 1
        
        print(current)
        
        for j in range(0, len(apple_rocation)):
            if current[1] == apple_rocation[j]:
                snake_length += 1                
                snake_record.append(current[1])
        
        take_time += 1
        
        for k in range(0, len(snake_record)):
            if current[1] == snake_record[k]:
                end == 1
                break;
                
        if current[1][0] == 0 or current[1][0] == game_map_size:
            end == 1
            break;
            
        if current[1][1] == 0 or current[1][1] == game_map_size:
            end == 1
            break;
                

#사과를 먹으면 몸 길이기 늘어나고













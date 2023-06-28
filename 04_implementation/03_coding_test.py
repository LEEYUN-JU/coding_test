# -*- coding: utf-8 -*-
"""
Created on Tue May 16 09:57:09 2023

@author: labpc
"""
       
#상하좌우

import numpy as np
import random
import copy

mx = np.random.randint(3, 9)
my = np.random.randint(3, 9)

direction = np.random.randint(0, 4) 

game_map = []

for j in range(my):
    if j == 0:
        game_map.append([1 for _ in range(mx)])
    
    if j > 0 and j < my-1:
        game_map_mid = []
        for i in range(mx):
            if i == 0:
                game_map_mid.append(1)
            if i > 0 and i < mx-1:
                game_map_mid.append(np.random.randint(0, 2))
            if i == mx-1:
                game_map_mid.append(1)
        
        game_map.append(game_map_mid)
        
    if j == my-1:
        game_map.append([1 for _ in range(mx)])

while True:
    ix = np.random.randint(0, mx-1)
    iy = np.random.randint(0, my-1)
    
    if game_map[iy][ix] == 0:
        break
    else:
        continue
        
        
move_count = 0

def turn_left(direction):
    
    if direction == 0:
        direction = 3
      
    if direction == 1:
        direction = 0
        
    if direction == 2:
        direction = 1
        
    if direction == 3:
        direction = 2
        
    return direction

def move(ix, iy, direction):
    if direction == 0:
        iy = iy - 1       
      
    if direction == 1:
        ix = ix - 1        
        
    if direction == 2:
        iy = iy + 1
        
    if direction == 3:
        ix = ix + 1
        
    if game_map[iy][ix] == 1:
        return 0, 0
    else:
        return ix, iy
    

moved_map = copy.deepcopy(game_map)
turn_time = 0

#우선 방향 바꾸기
direction = turn_left(direction)

while True:         
    print(iy, ix, direction)    
    
    #방향별로 갈수 있는 경우
    if direction == 0:
        if moved_map[iy-1][ix] == 0:
            iy = iy - 1
            move_count += 1
            moved_map[iy][ix] = 1
            turn_time = 0
            
        else:
            turn_time += 1
            direction = 3
                
    if direction == 1:
         if moved_map[iy][ix+1] == 0:
             ix = ix + 1
             move_count += 1
             moved_map[iy][ix] = 1
             turn_time = 0
             
         else:
             turn_time += 1  
             direction = 0
                 
    if direction == 2:
        if moved_map[iy+1][ix] == 0:
            iy = iy + 1
            move_count += 1
            moved_map[iy][ix] = 1
            turn_time = 0
            
        else:
            turn_time += 1         
            direction = 1                    

                 
    if direction == 3:
         if moved_map[iy][ix-1] == 0:
             ix = ix - 1
             move_count += 1
             moved_map[iy][ix] = 1
             turn_time = 0
             
         else:
             turn_time += 1  
             direction = 2
             
    if turn_time == 4:
        ix, iy = move(ix, iy, direction)        
        move_count += 1
        if ix == 0:
            break
        
        turn_time = 0
                 
           
           
            
        
        
           
            
        
            
            
        
            
            
            
            
            
            
            
            
            
            
            
            

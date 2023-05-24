# -*- coding: utf-8 -*-
"""
Created on Tue May 16 09:57:09 2023

@author: labpc
"""
       
#상하좌우

import numpy as np
import random

person = [1, 1]

n = np.random.randint(1, 100)

trip_map = [[0 for j in range(n)] for i in range(n)]

move = np.random.randint(0, 4)

# 0 = L
# 1 = R
# 2 = U
# 3 = D

root_size = np.random.randint(1, 100)

move_root = []

for i in range(root_size):
    move_root.append(np.random.randint(0, 4))

for move in move_root:
    if move == 0:
        if person[1] > 1:
            person[1] = person[1] - 1
        else:
            person[1] = person[1]
        
    if move == 1:
        if person[1] < n-1: 
            person[1] = person[1] + 1
        else:
            person[1] = person[1]
            
    if move == 2:
        if person[0] > 1: 
            person[0] = person[0] - 1
        else:
            person[0] = person[0]
            
    if move == 3:
        if person[0] < n-1: 
            person[0] = person[0] + 1
        else:
            person[0] = person[0]

move_types = []
print("trip_size: %d"%n)   

for move_type in move_root:
    if move_type == 0:
        move_types.append("L")
    if move_type == 1:
        move_types.append("R")
    if move_type == 2:
        move_types.append("U")
    if move_type == 3:
        move_types.append("D")
    
print(move_types)
print(person[0], person[1])










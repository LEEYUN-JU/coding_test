# -*- coding: utf-8 -*-
"""
Created on Tue May 16 09:57:09 2023

@author: labpc
"""
       
#왕실의 나이트

import numpy as np
import random

x = np.random.randint(1, 9)
y = np.random.randint(1, 9)

dy = ['up', 'down']
dx = ['left', 'right']

possible = 0

for up_down in dy:
    for left_right in dx:
        if up_down == 'up' and left_right == 'left':
            ny = y + 2
            nx = x - 1
        
        if up_down == 'up' and left_right == 'right':
            ny = y + 2
            nx = x + 1
            
        if up_down == 'down' and left_right == 'left':
            ny = y - 2
            nx = x - 1
            
        if up_down == 'down' and left_right == 'right':
            ny = y - 2
            nx = x + 1
                    
        if nx > 8 or nx < 1 or ny > 8 or ny <1:
            continue
        else:
            possible += 1
            
for left_right in dx:
    for up_down in dy:    
        if up_down == 'up' and left_right == 'left':
            ny = y + 1
            nx = x - 2
        
        if up_down == 'up' and left_right == 'right':
            ny = y + 1
            nx = x + 2
            
        if up_down == 'down' and left_right == 'left':
            ny = y - 1
            nx = x - 2
            
        if up_down == 'down' and left_right == 'right':
            ny = y - 1
            nx = x + 2
                    
        if nx > 8 or nx < 1 or ny > 8 or ny <1:
            continue
        else:
            possible += 1

print(possible)






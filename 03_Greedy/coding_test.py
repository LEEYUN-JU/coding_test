# -*- coding: utf-8 -*-
"""
Created on Tue May 16 09:57:09 2023

@author: labpc
"""
       
#

import numpy as np
import random
import copy

n = np.random.randint(1, 1001)

bowling = []

for i in range(0, n):
    bowling.append(np.random.randint(1, 11))

select = []

for i in range(0, n):
    for j in range(i, n):
        select.append([i, j])

print(len(select))
            
        
        
           
            
        
            
            
        
            
            
            
            
            
            
            
            
            
            
            
            
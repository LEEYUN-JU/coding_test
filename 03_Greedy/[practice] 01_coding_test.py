# -*- coding: utf-8 -*-
"""
Created on Tue May 16 09:57:09 2023

@author: labpc
"""
       
#상하좌우

import numpy as np
import random
import copy

n = np.random.randint(1, 100)

x = []

for i in range(n):
    x.append(np.random.randint(1, n))

x.sort()

sum_of_team = 0

print("n : ", n)

for i in range(0, len(x)):
    
    n = n - x[i]
    if n < 0:
        n = n + x[i]
        break
    else:
        sum_of_team += 1
    
        
    print(n)
    




           
           
            
        
        
           
            
        
            
            
        
            
            
            
            
            
            
            
            
            
            
            
            

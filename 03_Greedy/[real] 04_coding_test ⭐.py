# -*- coding: utf-8 -*-
"""
Created on Tue May 16 09:57:09 2023

@author: labpc
"""
       
#

import numpy as np
import random
import copy

n = np.random.randint(1, 1000)

coins = []

for i in range(0, n):
    coins.append(np.random.randint(1, 1000000))

cases = []

for j in range(0, n):
    for k in range(0, n):
        cases.append(coins[j] + coins[k])
        
cases.sort()

for i in range(1, n):
    if i != cases[i]:
        print(i)
        break
    
    else:
        continue

        
           
            
        
        
           
            
        
            
            
        
            
            
            
            
            
            
            
            
            
            
            
            

# -*- coding: utf-8 -*-
"""
Created on Tue May 16 09:57:09 2023

@author: labpc
"""
       
#

import numpy as np
import random
import copy
import heapq

while True:

    score = np.random.randint(10, 100000000)
    
    if len(str(score)) % 2 != 0:
        score = np.random.randint(10, 100000000)
    
    else:
        break
                
cut = int(len(str(score)) / 2)

front = str(score)[0:cut]
back = str(score)[cut:]

front_sum = 0
back_sum = 0

for i in range(cut):
    front_sum += int(str(score)[0:cut][i])
    back_sum += int(str(score)[cut:][i])
    

if front_sum == back_sum:    
    print("LUCKY")

else:
    print("READY")
            
            
            
            
            
            
            
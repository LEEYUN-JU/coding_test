# -*- coding: utf-8 -*-
"""
Created on Tue May 16 09:57:09 2023

@author: labpc
"""
       
#상하좌우

import numpy as np
import random

n = np.random.randint(0, 23)

num_3_count = 0

for i in range(n+1):    
        
    for j in range(60):       
            
        for k in range(60):
            if '3' in str(i) + str(j) + str(k):
                num_3_count += 1
                
print(num_3_count)









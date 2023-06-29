# -*- coding: utf-8 -*-
"""
Created on Tue May 16 09:57:09 2023

@author: labpc
"""
       
#상하좌우

import numpy as np
import random
import copy

n = np.random.randint(1, 20)

num = []
st = ''

for i in range(n):
    temp = np.random.randint(0, 9)
    num.append(temp)
    st += str(temp)

num.sort(reverse=True)

total = 1

for j in range(0, len(num)):
    if num[j] == 0 and j == 0:
        total = 0
    
    if num[j] > 1:
        temp_total = total * num[j]
        
        if temp_total > 2000000000:
            total = total + num[j]
        else:
            total = temp_total
        
        
    else:
        total = total + num[j]
        
print(total)
    

           
           
            
        
        
           
            
        
            
            
        
            
            
            
            
            
            
            
            
            
            
            
            

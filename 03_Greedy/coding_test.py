# -*- coding: utf-8 -*-
"""
Created on Tue May 16 09:57:09 2023

@author: labpc
"""
#큰 수의 법칙
import numpy as np
import random

n = np.random.randint(2, 10)
m = np.random.randint(1, 10)
k = np.random.randint(1, 10)

data = []

for value in range(n):
    data.append(random.randint(0, 5))

num_type = list(set(data))

big = num_type[-1]
second_big = num_type[-2]

result = 0

k_2 = k

for i in range(m):            
    if k_2 > 0:        
        result += big
        k_2 = k_2 - 1       
    else:        
        result += second_big
        k_2 = k
       
    
        
        
        
        
    

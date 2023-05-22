# -*- coding: utf-8 -*-
"""
Created on Tue May 16 09:57:09 2023

@author: labpc
"""
       
#1이 될때까지

import numpy as np
import random

n = np.random.randint(2, 100000)
k = np.random.randint(2, 100000)

while True:
    if n < k:
        k = np.random.randint(1, 5)
    else:
        break

count = 0
first = n

while True:   
    
    if n % k == 0:
        n = n / k
        count += 1

    else:
        n = n -1 
        count += 1
        
    if n == 1:
        break










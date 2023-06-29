# -*- coding: utf-8 -*-
"""
Created on Tue May 16 09:57:09 2023

@author: labpc
"""
       
#문자열 뒤집기 - 모르겠어서 코드 참조함

import numpy as np
import random
import copy

n = np.random.randint(1, 1000000)

num = []
st = ''

for i in range(n):
    temp = np.random.randint(0, 2)
    num.append(temp)
    st += str(temp)

#num.sort(reverse=True)

count_0 = 0
count_1 = 1

for i in range(0, len(num)-1):
    if num[i] != num[i+1]:
        # 다음 수에서 1로 바뀌는 경우
        if num[i+1] == 1:
            count_0 += 1
        
        # 다음 수에서 0으로 바뀌는 경우
        else:
            count_1 += 1
            
print(min(count_0, count_1))
        
        
           
            
        
        
           
            
        
            
            
        
            
            
            
            
            
            
            
            
            
            
            
            
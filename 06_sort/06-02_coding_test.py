from collections import deque
import numpy as np
import random

n = 3

temp = [15,27,12]

for i in range(n-1):
    
    if temp[i] < temp[i+1]:
        temp[i], temp[i+1] = temp[i+1], temp[i]
        
    else:
        pass

   

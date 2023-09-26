from collections import deque
import numpy as np
import random
import heapq

x = 26
cal = 1

x -= 1

while x != 1:
    
    if x % 2 == 0:
        x = x / 2
        cal += 1
    
    elif x % 3 == 0:
        x = x / 3
        cal += 1
    
    elif x % 5 == 0:
        x = x / 5
        cal += 1
        
    else:
        x -= 1
    
print(cal)
#-----------------------------------------------------------------------------------------#   
















        
            
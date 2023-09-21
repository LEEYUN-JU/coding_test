from collections import deque
import numpy as np
import random
import heapq

n = 5
parts = [8, 3, 7, 9, 2]

m = 3
request = [5, 7, 9]

result = []

yes_or_no = 0

for i in request:
    for j in parts:
        if i == j:
            yes_or_no = 1
            break
        else:
            yes_or_no = 0
            
    if yes_or_no == 1:
        result.append("yes")
    else:
        result.append("no")
            

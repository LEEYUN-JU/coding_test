#숫자 카드 게임

import numpy as np
import random

n = np.random.randint(1, 5)
m = np.random.randint(1, 5)

data = [[0 for j in range(m)] for i in range(n)]

for i in range(n):
    for j in range(m):        
        data[i][j]=random.randint(1, 5)

minimum = sum(max(data))
min_line = []
    
for i in range(0, n):
    if min(data[i]) <= minimum:
        minimum = min(data[i])       
        min_line.append(i)
        
sum_data = sum(min_line)
result = sum(range(0, len(data)))-sum_data
final_result = max(data[result])
    



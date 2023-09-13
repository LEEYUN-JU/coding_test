from collections import deque
import numpy as np
import random

n = 4

house_ori = [5,1,7,9] 
antena = []
                
for i in range(n):
    house = house_ori.copy()    
    start = house.pop(i)
    temp = house.copy()
    summ = 0
    
    for j in range(len(temp)):
        summ += (abs(start - temp[j]))

    antena.append([summ, start])
    
antena = sorted(antena, key=lambda house:house[0])   

print(antena[0][1])

#아래는 정답 코드
n = int(input())
data = list(map(int, input().split()))
data.sort()

#중간값(median)을 출력
print(data[(n-1) // 2])



from collections import deque
import numpy as np
import random
import heapq

n = 3

set_order = [10, 20, 40] 

set_order = sorted(set_order)

be_sum = set_order[0] + set_order[1]

summation = 0

for i in range(0, len(set_order)):

        
    summation += set_order[i]

summation += be_sum

#아래는 정답 코드 
# import heapq를 이용한다
#힙에 초기 카드 묶음을 모두 삽입

heap = []
for i in range(n):
    data = int(input())
    heapq.heappush(heap, data)
    
result = 0

#힙에 원소가 1개 남을때까지
while len(heap) != 1:
    #가장 작은 2개의 카드 묶음 꺼내기
    one = heapq.heappop(heap)
    two = heapq.heappop(heap)
    #카드 묶음을 합쳐서 다시 삽입
    sum_value = one + two
    result += sum_value
    heapq.heappush(heap, sum_value)
    
print(result)
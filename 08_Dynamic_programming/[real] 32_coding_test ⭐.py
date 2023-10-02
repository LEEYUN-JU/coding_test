from collections import deque
import numpy as np
import random
import heapq

n = 5

tri = [[7],[3,8],[8,1,0],[2,7,4,4],[4,5,2,6,5]]

#다이나믹 프로그래밍을 위한 2차원 DP테이블 초기화
dp = tri

#다이나믹 프로그래밍 진행
for i in range(1, n):
    for j in range(i + 1):
        #왼쪽 위에서 오는 경우
        if j == 0:
            left_up = 0
        else:
            left_up = dp[i-1][j-1]
            
        #바로 위에서 오는 경우
        if j == i:
            down = 0
        else:
            down = dp[i-1][j]
            
        #최대 합을 저장
        dp[i][j] = dp[i][j] + max(left_up, down)
    
    
print(max(dp[n-1]))

#-----------------------------------------------------------------------------------------#   

from collections import deque
import numpy as np
import random
import heapq

#피보나치 함수(Fibonacchi Function)을 재귀 함수로 구현
def fibo(x):
    if x == 1 or x ==2 :
        return 1
    return fibo(x-1) + fibo(x-2)

print(fibo(4))

#위 방식은 숫자가 커질수록 시간 복잡도가 증가한다는 치명적인 단점을 가지고 있다.
#이에 메모이제이션 기법을 사용해보고자 한것이, 하기 코드이다.

#-----------------------------------------------------------------------------------------#   
#한 번 계산된 결과를 메모이제이션(Memoization)하기 위한 리스트 초기화. Top-down 방식
#메모이제이션은 top-down방식에만 사용된다.
d = [0] * 100

#피보나치 함수(Fibonacchi Function)를 재귀함수로 구현(탑다운 다이나믹 프로그래밍)
def fibo(x):
    #종료 조건(1 혹은 2일 때 1을 반환)
    if x == 1 or x == 2:
        return 1
    
    #이미 계산한 적 있는 문제라면 그대로 반환
    if d[x] != 0:
        return d[x]
    
    #아직 계산하지 않은 문제라면 점화식에 따라서 피보나치 결과 반환
    d[x] = fibo(x-1) + fibo(x-2)
    return d[x]

print(fibo(99))

#-----------------------------------------------------------------------------------------#   
#호출 되는 함수를 직접 print 하여 확인함으로써, 얼마나 효율적인지 확인한다
d = [0] * 100

def pibo(x):
    print('f(' + str(x) + ')', end=' ')
    if x == 1 or x == 2:
        return 1
    if d[x] != 0:
        return d[x]
    d[x] = pibo(x-1) + pibo(x-2)
    return d[x]

pibo(6)

#-----------------------------------------------------------------------------------------#   
#동일한 원리를 적용하되 단순히 반복문을 이용하여 문제를 해결하는 방법인 bottom-up 방식
#앞서 계산된 결과를 저장하기 위한 DP 테이블 ㅈ초기화
d = [0] * 100

#첫 번재 피보나치 수와 두 번째 피보나치 수는 1
d[1] = 1
d[2] = 2
n = 99

#피보나치 함수(Fibonacci Function) 반복문으로 구현(보텀업 다이나믹 프로그래밍)
for i in range(3, n+1):
    d[i] = d[i-1] + d[i-2]
    
print(d[n])
















        
            

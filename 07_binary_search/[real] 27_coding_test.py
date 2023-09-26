from collections import deque
import numpy as np
import random
import heapq

n = 7
x = 4

lisst = [1,1,2,2,2,2,3]
nums = 0

if lisst.count(x) == True:
    nums = lisst.count(x)
    
else:
    nums = -1

print(nums)
     
#-----------------------------------------------------------------------------------------#   
#아래는 정답 코드
#정렬된 수열에서 값이 x인 원소의 개수를 세느 ㄴ메서드
def count_by_value(array, x):
    #데이터의 개수
    n = len(array)
    
    #x가 처음 등장한 인덱스 계산
    a = first(array, x, 0, n-1)
    
    #수열에 x가 존재하지 않는 경우
    if  a== None:
        return 0 #값이 x인 원소의 개수는 0개이므로 0 반환
    
    #x가 마지막으로 등장한 인덱스 계산
    b = last(array, x, 0, n-1)
    
    #개수를 반환
    
#처음 위치를 찾는 이진 탐색 메서드
def first(array, target, start, end):
    if start > end:
        return None
    
    mid = (start + end) // 2
    #해당 값을 가지는 원소 중에서 가장 왼쪽에 있는 경우에만 인덱스 반환
    if (mid == 0 or target> array[mid-1]) and array[mid] == target:
        return mid
    
    #중간점의 값 보다 찾고자 하는 값이 작거나 같은 경우 왼쪽 확인
    elif array[mid] >= target:
        return first(array, target, start, mid-1)
    
    #중간점의 값 보다 찾고자 하는 값이 큰 경우 오른쪽 확인
    else:
        return first(array, target, mid + 1, end)
    
#마지막 위치를 찾는 이진 탐색 메서드
def last(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    
    #해당 값을 가지는 원소 중에서 가장 왼쪽에 있는 경우에만 인덱스 반환
    if (mid == n -1 or target < array[mid+1]) and array[mid] == target:
        return mid
    
    #중간점의 값 보다 찾고자 하는 값이 작거나 같은 경우 왼쪽 확인
    elif array[mid] > target:
        return first(array, target, start, mid-1)
    
    #중간점의 값 보다 찾고자 하는 값이 큰 경우 오른쪽 확인
    else:
        return first(array, target, mid + 1, end)
    
n, x = map(int, input().split()) #데이터의 개수 N, 찾고자 하는 값 x를 입력받기
array = list(map(int, input().split())) #전체 데이터 입력받기

#값이 x인 데이터의 개수 계산
count = count_by_value(array, x)

#값이 x인 원소가 존재하지 않는다면
if count == 0:
    print(-1)
    
#값이 x인 원소가 존재한다면
else:
    print(count)

#-----------------------------------------------------------------------------------------#
#단순히 정렬된 수열에서 특정한 값을 가지는 원소의 개수를 구하는 문제이므로, 파이썬의 이진 탐색
#라이브러리인 bisect을 적절히 활용하면 손쉽게 문제 해결이 가능하다.

from bisect import bisect_left, bisect_right

#값이 [left_value, right_value]인 데이터의 개수를 반환하는 함수
def count_by_range(array, left_value, right_value):
    right_index = bisect_right(array, right_value)
    left_index = bisect_left(array, left_value)
    return right_index - left_index

n, x = map(int, input().split()) #데이터의 개수 N, 찾고자 하는 값 x를 입력받기
array = list(map(int, input().split())) #전체 데이터 입력받기

#값이 [x, x] 범위에 있는 데이터의 개수 계산
count = count_by_range(array, x, x)

#값이 x인 원소가 존재하지 않는다면
if count == 0:
    print(-1)
    
#값이 x인 원소가 존재한다면
else:
    print(count)
















        
            
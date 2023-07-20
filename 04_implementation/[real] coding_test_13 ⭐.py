import numpy as np
import random

map_size = np.random.randint(2, 51)
store_size = np.random.randint(1, 14)

home_count = np.random.randint(1, 2*map_size)
store_count = np.random.randint(store_size, 14)

whole_map = []

map_info = []

home = []
store = []

for i in range(0, home_count):
    home.append(1)

for j in range(0, store_count):
    store.append(2)
    
for p in range(0, (map_size**2)-home_count-store_count):
    map_info.append(0)
    
whole_map = home + store + map_info

random.shuffle(whole_map)
whole_map = np.resize(whole_map, [map_size, map_size])



house_map = []
chicken_map = []

for i in range(0, map_size):
    for j in range(0, map_size):
        if whole_map[i][j] == 1:
            house_map.append([i, j])
        if whole_map[i][j] == 2:
            chicken_map.append([i, j])

del_info = []

for i in range(0, len(chicken_map)):
    for j in range(0, len(house_map)):
        del_info.append( abs(chicken_map[i][0]-house_map[j][0] + chicken_map[i][1]-house_map[j][1]))





############# 여기서 부터는 정답 코드###################
from itertools import combinations

n, m = map(int, input().split())
chicken, house = [], []

for r in range(n):
    data = list(map(int, input().split()))
    for c in range(n):
        if data[c] == 1:
            house.append((r, c))
        elif data[c] == 2:
            chicken.append((r, c))
            
#모든 치킨집 중에서 m개의 치킨집을 뽑는 조합 계산
candidates = list(combinations(chicken, m))

#치킨 거리의 합을 계산하는 함수
def get_sum(candidate):
    result = 0
    #모든 집에 대하여
    for hx, hy in house:
        #가장 가까운 치킨집을 찾기
        temp = 1e9
        for cx, cy in candidate:
            temp = min(temp, abs(hx - cx) + abs(hy - cy))
        #가장 가까운 치킨집까지의 거리를 더하기
        result += temp
    
    #치킨 거리의 합 반환
    return result

#치킨 거리의 합의 최소를 찾아 출력
result = 1e9
for candidate in candidates:
    result = min(result, get_sum(candidate))
    
print(result)

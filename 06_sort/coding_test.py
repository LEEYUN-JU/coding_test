from collections import deque
import numpy as np
import random

n = 12

grade = [['Jyunkyu', 50, 60, 100], ['Sangkeun', 80, 60, 50], ['Sunyoung', 80, 70, 100], ['Soong',50,60,90], ['Haebin',50,60,100],
         ['Kangsoo',60,80,100],['Donghyuk',80,60,100],['Sei',70,70,70],['Wonseob',70,70,90],['Sanghyun',70,70,80],
         ['nsj',80,80,80],['Taewhan',50,60,90]]
                
    
grade = sorted(grade, key=lambda x: (-int(x[1]), (int(x[2]), (-int(x[3]), x[0]))))   

#아래는 정답 코드
#grade.sort(key=lambda x: (-int(x[1]), (int(x[2]), (-int(x[3]), x[0]))))   
#데이터 셋이 set으로 구성되어 있는 경우 사용 가능하다고 한다
#grade[('Jyunkyu', 50, 60, 100), ***, ('Taewhan',50,60,90)]

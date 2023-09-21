#https://school.programmers.co.kr/learn/courses/30/lessons/42889 > 프로그래머스 카카오 2019 기출문제

def solution(N, stages):
    #우선 정렬하기
    stages = sorted(stages)
    
    #각 스테이지 별로 실패율 구하기
    failue = []
    peo = len(stages)
    
    for i in range(N):
        st = 0        
        for j in stages:
            if i+1 == j:
                st += 1                
        
        if i == 0:
            failue.append([i+1, round(st/peo, 3)])
            peo = peo - st
        
        else:
            if peo != 0:
                failue.append([i+1, round(st/peo, 3)])
            else:
                failue.append([i+1, 0])
                
            peo = peo - st
                
    
    failue = sorted(failue, key=lambda chart:chart[1], reverse=True)
    print(failue)
        
    answer = []
    for i in failue:
        answer.append(i[0])
    
    return answer

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


#아래는 정답 코드
def solution(N, stages):
    answer = []
    length = len(stages)
    
    #스테이지 번호를 1부터 N까지 증가시키며 
    for i in range(1, N+1):
        #해당 스테이지에 머물러 있는 사람의 수 계산
        count = stages.count(i)
        
        #실패율 계산
        if length == 0:
            fail = 0
        else:
            fail = count / length
            
        #리스트에 (스테이지 번호, 실패율) 원소 삽입
        answer.append((i, fail))
        length -= count
        
    #실패율을 기준으로 각 스테이지를 내림차순 정렬
    answer = sorted(answer, key=lambda t:t[1], reverse=True)
    
    #정렬된 스테이지 번호 출력
    answer = [i[0] for i in answer]
        
    return answer

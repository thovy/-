def solution(s):
    answer = 0
    
    cnta, cntb = 0, 0
    for i in s:
        if cnta == cntb:
            answer += 1
            fw = i
        
        if i == fw:
            cnta += 1
        else:
            cntb += 1            
    
    return answer
def solution(n, m, section):
    answer = 0
    
    sec_init = section.pop(0)
    painting = sec_init + m-1
    answer += 1
    while section:
        sec = section.pop(0)
        if sec <= painting:
            continue
        else:
            painting = sec + m-1
            answer += 1
            
        
    
    return answer
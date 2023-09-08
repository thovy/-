def solution(sizes):
    answer = 0
    
    w_max = 0
    h_max = 0
    
    for w, h in sizes:
        if w < h:
            w, h = h, w
        
        if w > w_max:
            w_max = w
        if h > h_max:
            h_max = h
    
    answer = w_max * h_max
    
    return answer
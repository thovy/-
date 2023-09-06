def solution(dots):
    
    johab = [[[1,2],[3,4]], [[1,3],[2,4]], [[1,4],[2,3]]]
    for j in johab:
        line1_x = abs(dots[j[0][0]-1][0] - dots[j[0][1]-1][0])
        line1_y = abs(dots[j[0][0]-1][1] - dots[j[0][1]-1][1])
        line2_x = abs(dots[j[1][0]-1][0] - dots[j[1][1]-1][0])
        line2_y = abs(dots[j[1][0]-1][1] - dots[j[1][1]-1][1])
        
        if line1_x/line1_y == line2_x/line2_y:
            return 1
    
    return 0
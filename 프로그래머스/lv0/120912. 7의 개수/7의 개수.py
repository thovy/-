def solution(array):
    answer = 0
    for a in array:
                
        while a>10:
            num = a % 10
            a = a // 10
            if num == 7:
                answer += 1
        if a< 10:
            if a == 7:
                answer += 1
            
    return answer
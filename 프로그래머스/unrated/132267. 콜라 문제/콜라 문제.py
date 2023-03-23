import math
def solution(a, b, n):
    answer = 0
    
    while n >= a:
        answer += (n//a)*b
        n = b*(n//a) + math.ceil(n%a)
    
    return answer
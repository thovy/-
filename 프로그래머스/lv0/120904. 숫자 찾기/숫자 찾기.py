def solution(num, k):
    answer = 0
    if str(k) not in str(num):
        return -1
    
    return str(num).index(str(k)) + 1
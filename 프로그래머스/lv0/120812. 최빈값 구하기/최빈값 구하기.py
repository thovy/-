def solution(array):
    
    answer = 0
    
    
    count_list = [0] * (max(array)+1)
    for a in array:
        count_list[a] += 1
    answer = count_list.index(max(count_list))
    if count_list.count(max(count_list)) >= 2:
        return -1
    
    return answer
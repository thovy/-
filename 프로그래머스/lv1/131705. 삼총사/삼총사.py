from itertools import combinations, permutations

def solution(number):
    answer = 0
    
    # # 중복 X
    # print(list(combinations(number, 3)))
    # # 모든 경우
    # print(list(permutations(number, 3)))
    
    combi = list(combinations(number, 3))
    for c in combi:
        if sum(c) == 0:
            answer += 1
    
    
    return answer
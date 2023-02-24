def solution(bridge_length, weight, truck_weights):
    answer = 0
    
    onbrg = [0]*bridge_length
    onbrg_weight = 0
    while True:
        onbrg_weight += onbrg[-1]
        onbrg_weight -= onbrg[0]
        if truck_weights:
            answer += 1
            # if truck_weights[0] + sum(onbrg) - onbrg[0] <= weight:
            if truck_weights[0] + onbrg_weight <= weight:
                onbrg.pop(0)
                t = truck_weights.pop(0)
                onbrg.append(t)
            else:
                onbrg.pop(0)
                onbrg.append(0)
        elif sum(onbrg) != 0:
            answer += 1
            onbrg.pop(0)
            onbrg.append(0)
        else:
            return answer
        
# 정확성  테스트
# 테스트 1 〉	통과 (37.68ms, 10.2MB)
# 테스트 2 〉	통과 (1862.49ms, 10.3MB)
# 테스트 3 〉	통과 (0.04ms, 10.2MB)
# 테스트 4 〉	통과 (365.53ms, 10.2MB)
# 테스트 5 〉	실패 (시간 초과)
# 테스트 6 〉	통과 (2857.53ms, 10.2MB)
# 테스트 7 〉	통과 (9.05ms, 10.3MB)
# 테스트 8 〉	통과 (0.24ms, 10.4MB)
# 테스트 9 〉	통과 (6.43ms, 10.3MB)
# 테스트 10 〉	통과 (0.30ms, 10.3MB)
# 테스트 11 〉	통과 (0.01ms, 10.3MB)
# 테스트 12 〉	통과 (0.29ms, 10.3MB)
# 테스트 13 〉	통과 (1.91ms, 10.3MB)
# 테스트 14 〉	통과 (0.11ms, 10.3MB)
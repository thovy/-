def solution(bridge_length, weight, truck_weights):
    answer = 0
    
    onbrg = [0]*bridge_length
    onbrg_weight = 0
    while True:
        # sum 을 사용하면 테스트 5번이 시간초과 나옴.
        onbrg_weight += onbrg[-1]
        onbrg_weight -= onbrg[0]
        if truck_weights:
            answer += 1
            # if truck_weights[0] + sum(onbrg) - onbrg[0] <= weight:
            # onbrg_weight 를 사용할 땐 - onbrg[0] 을 하면 안 됨. 나갈 트럭 무게가 두 번 빠지게 되는 것.
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

# sum 을 쓰지 않으니 훨씬 빠르다. 5번도 통과함
# 정확성 테스트
# 테스트 1 〉	통과 (16.59ms, 10.2MB)
# 테스트 2 〉	통과 (399.98ms, 10.3MB)
# 테스트 3 〉	통과 (0.04ms, 10.2MB)
# 테스트 4 〉	통과 (38.27ms, 10.2MB)
# 테스트 5 〉	통과 (456.88ms, 10.2MB)
# 테스트 6 〉	통과 (115.61ms, 10.2MB)
# 테스트 7 〉	통과 (2.69ms, 10.2MB)
# 테스트 8 〉	통과 (0.13ms, 10.2MB)
# 테스트 9 〉	통과 (2.77ms, 10.2MB)
# 테스트 10 〉	통과 (0.14ms, 10.3MB)
# 테스트 11 〉	통과 (0.01ms, 10.2MB)
# 테스트 12 〉	통과 (0.20ms, 10.2MB)
# 테스트 13 〉	통과 (0.80ms, 10.2MB)
# 테스트 14 〉	통과 (0.09ms, 10.2MB)

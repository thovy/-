def solution(answers):
    answer = []
    
    supo1 = [1,2,3,4,5]
    supo2 = [2, 1, 2, 3, 2, 4, 2, 5]
    supo3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    score = {1:0, 2:0, 3:0}
    
    for idx in range(len(answers)):
        if supo1[idx % len(supo1)] == answers[idx]:
            score[1] += 1
        if supo2[idx % len(supo2)] == answers[idx]:
            score[2] += 1
        if supo3[idx % len(supo3)] == answers[idx]:
            score[3] += 1
    
    max_score = max(score.values())
    
    for k, v in score.items():
        if v == max_score:
            answer.append(k)
    
    return answer
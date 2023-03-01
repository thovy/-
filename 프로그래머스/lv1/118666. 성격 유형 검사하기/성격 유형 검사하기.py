def checkscore(score, surv, choice):
    if choice == 4:
        return
    elif choice < 4:
        score[surv[0]] += 4-choice
    elif choice > 4:
        score[surv[1]] += choice-4
    
def solution(survey, choices):
    answer = ''
    checktype = ['R','T','C','F','J','M','A','N']
    
    score = {'R':0, 'T':0, 'C':0, 'F':0, 'J':0, 'M':0, 'A':0, 'N':0}
    for i in range(len(survey)):
        checkscore(score, survey[i], choices[i])
    
    for i in range(0,8,2):
        if score[checktype[i]] >= score[checktype[i+1]]:
            answer += checktype[i]
        elif score[checktype[i]] < score[checktype[i+1]]:
            answer += checktype[i+1]
    return answer
def checkrank(answer, count):
    if count == 6:
        answer.append(1)
    elif count == 5:
        answer.append(2)
    elif count == 4:
        answer.append(3)
    elif count == 3:
        answer.append(4)
    elif count == 2:
        answer.append(5)
    elif count == 1:
        answer.append(6)
    elif count == 0:
        answer.append(6)
            
def solution(lottos, win_nums):
    answer = []
    
    countwin = 0
    for i in win_nums:
        countwin += lottos.count(i)
    
    zerocnt = lottos.count(0)
    bestwin = countwin + zerocnt
    
    checkrank(answer, bestwin)
    checkrank(answer, countwin)
    
    return answer
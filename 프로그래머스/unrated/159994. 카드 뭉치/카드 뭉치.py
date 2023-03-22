def solution(cards1, cards2, goal):
    answer = 'Yes'
    
    def check(g, card1, card2):
        if g == card1:
            if not goal:
                tmp = 'Yes'
                return tmp
            elif len(cards1) == 0:
                tmp = check(goal.pop(0), "", card2)
            else:
                tmp = check(goal.pop(0), cards1.pop(0), card2)
        elif g == card2:
            if not goal:
                tmp = 'Yes'
                return tmp
            elif len(cards2) == 0:
                tmp = check(goal.pop(0), card1, "")
            else:
                tmp = check(goal.pop(0), card1, cards2.pop(0))
        else:
            return 'No'
        
        return tmp

    if goal and cards1 and cards2:
        answer = check(goal.pop(0), cards1.pop(0), cards2.pop(0))
    
    return answer
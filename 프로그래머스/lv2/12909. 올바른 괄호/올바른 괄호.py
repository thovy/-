from collections import deque
def solution(s):
    answer = True
    
    q = deque()
    
    if s[0] == ")" or s[-1] == "(":
        answer = False
    elif s.count("(") != s.count(")"):
        answer = False
    # else:
        # for i in len(s):
        #     if s[i] == ')' and i <:
        
    tmp = 0
    for i in range(len(s)):
        if s[i] == ")":
            tmp -= 1
        else:
            tmp += 1
        
        if tmp < 0:
            return False
    
    return answer
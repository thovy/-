def solution(s):
    answer = True
    
    if s[0] == ")" or s[-1] == "(":
        answer = False
    elif s.count("(") != s.count(")"):
        answer = False
        
    tmp = 0
    for i in range(len(s)):
        if s[i] == ")":
            tmp -= 1
        else:
            tmp += 1
        
        if tmp < 0:
            return False
    
    return answer


#     answer = True
    
#     stack = [s[0]]
    
#     if s[0] == ")" or s[-1] == "(":
#         answer = False
#     elif s.count("(") != s.count(")"):
#         answer = False
        
#     for g in s[1:]:
#         tmp = ''
#         if stack:
#             tmp = stack.pop()
            
#         if tmp == '(' and g == '(':
#             stack.append(g)
#         elif tmp == '(' and g == ')':
#             continue
#         elif tmp == ')':
#             return False
        
#     if stack:
#         return False
    
#     return answer
            
    


# 정확성  테스트
# 테스트 1 〉	통과 (0.00ms, 10MB)
# 테스트 2 〉	통과 (0.00ms, 10.2MB)
# 테스트 3 〉	통과 (0.00ms, 10.2MB)
# 테스트 4 〉	통과 (0.00ms, 10.4MB)
# 테스트 5 〉	통과 (0.00ms, 10.2MB)
# 테스트 6 〉	통과 (0.00ms, 10.4MB)
# 테스트 7 〉	통과 (0.01ms, 10.1MB)
# 테스트 8 〉	통과 (0.00ms, 10.2MB)
# 테스트 9 〉	통과 (0.01ms, 10.1MB)
# 테스트 10 〉	통과 (0.01ms, 10.2MB)
# 테스트 11 〉	통과 (0.01ms, 10.2MB)
# 테스트 12 〉	통과 (0.02ms, 10MB)
# 테스트 13 〉	통과 (0.02ms, 10.2MB)
# 테스트 14 〉	통과 (0.01ms, 10.3MB)
# 테스트 15 〉	통과 (0.02ms, 10.2MB)
# 테스트 16 〉	통과 (0.02ms, 10.2MB)
# 테스트 17 〉	통과 (0.02ms, 10.3MB)
# 테스트 18 〉	통과 (0.01ms, 10MB)
# 효율성  테스트
# 테스트 1 〉	통과 (8.96ms, 10.2MB)
# 테스트 2 〉	통과 (9.98ms, 10.3MB)
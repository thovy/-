def solution(X, Y):
#     answer = ''
    
#     samelist = []
#     for i in range(len(X)):
        
#         if X[:len(X)-i-1] in Y and X[:len(X)-i-1] not in samelist:
#             samelist.append(X[:len(X)-i-1])
#             Y = Y.replace(X[:len(X)-i-1], '')
            
#     for i in range(len(X)):
#         if X[i:] in Y and X[i:] not in samelist:
#             samelist.append(X[i:])
#             Y = Y.replace(X[i:], '')
            
#     for i in range(len(X)):
#         if X[i] in Y and X[i] not in samelist:
#             samelist.append(X[i])
#             Y = Y.replace(X[i],'')
        
# #         if X[i] in Y and X[i] not in samelist:
# #             samelist.append(X[i])
    
#     samelist = sorted(samelist, reverse=True)
#     if not samelist or samelist[0] == '':
#         return "-1"
#     elif samelist[0] == "0":
#         return "0"
#     else:
#         for s in samelist:
#             answer += s

#         return answer

    x_count = {}
    y_count = {}
    
    # X와 Y의 숫자 등장 횟수를 계산합니다.
    for digit in X:
        x_count[digit] = x_count.get(digit, 0) + 1
    for digit in Y:
        y_count[digit] = y_count.get(digit, 0) + 1
    
    # 공통으로 나타나는 숫자를 찾습니다.
    common_digits = set(x_count.keys()) & set(y_count.keys())
    
    # 가장 큰 정수를 만듭니다.
    result = []
    for digit in sorted(common_digits, reverse=True):
        count = min(x_count[digit], y_count[digit])  # 공통으로 나타나는 숫자의 최소 등장 횟수
        result.extend([digit] * count)
    
    # 만들어진 최대 정수를 문자열로 변환하여 반환합니다.
    if not result:
        return "-1"
    elif result[0] == '0':
        return '0'
    return ''.join(result)
import numpy

def solution(s):
    answer = []
        
#     for idx, w in enumerate(s):
        
#         # w 앞에 있는 글자 tmp 에 넣고
#         tmp = s[:idx]
#         # numpy 사용을 위해 list 로 만들어서
#         tmplist = []
#         for t in tmp:
#             tmplist.append(t)
#         # 지금 글자가 앞 글자(tmp) 에 있으면
#         if w in tmp:
#             # list 를 array 로 만든 뒤, numpy 로 인덱스를 다 찾은 뒤에 max 로 최고값만 preidx 에 저장
#             preidx = max(numpy.where(numpy.array(tmplist)==w)[0])
#             # 지금 글자의 idx 와 preidx 비교해서 차이 step 을 answer 에 넣기
#             step = idx - int(preidx)
#             answer.append(step)
#         # 지금 글자가 앞 글자(tmp) 에 없으면
#         else:
#             answer.append(-1)
    
    
    
#     return answer

    dic = dict()
    for i in range(len(s)):
        if s[i] not in dic:
            answer.append(-1)
        else:
            answer.append(i - dic[s[i]])
        dic[s[i]] = i
        # print(dic)

    return answer
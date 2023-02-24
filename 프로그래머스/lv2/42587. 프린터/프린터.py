def solution(priorities, location):
    answer = 0
    q = [(idx, pri) for idx, pri in enumerate(priorities)]
    # maxnum = max(priorities)
    while True:
        tmp = q.pop(0)
        if any(tmp[1] < qt[1] for qt in q):
            q.append(tmp)
        else:
            answer += 1
            if location == tmp[0]:
                return answer
    # return answer
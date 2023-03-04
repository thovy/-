def solution(tickets):
    answer = []
    
    q = {i[0]:[] for i in tickets}
    for i in tickets:
        q[i[0]].append(i[1])

    print(q)
    
    for i in q.keys():
        q[i].sort()
        
    stack=['ICN']
    while stack:
        top = stack[-1]
        if top not in q or len(q[top]) == 0:
            answer.append(stack.pop())
        else:
            stack.append(q[top].pop(0))
    answer.reverse()
    
    return answer
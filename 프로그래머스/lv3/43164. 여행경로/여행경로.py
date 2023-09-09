def solution(tickets):
    answer = []
    
    # 출발지:[목적지리스트]
    q = {i[0]:[] for i in tickets}
    for i in tickets:
        q[i[0]].append(i[1])

    print(q)
    
    # 출발지마다 목적지를 정렬 - 알파벳 순서로 앞서는 경로를 return 하므로.
    for i in q.keys():
        q[i].sort()
    
    # 출발지는 ICN. 
    stack=['ICN']
    while stack:
        top = stack[-1]
        # 출발공항목록에 없거나 해당 공항에서 도착공항목록이 없으면, 마지막 공항으로 인식하고, answer에 저장.
        # 즉, else 문을 모두 돈 뒤(stack에 모두 쌓은 뒤) 하나씩 빼서 거꾸로 넣어주는 것.
        if top not in q or len(q[top]) == 0:
            answer.append(stack.pop())
        # 갈 곳이 있으면 도착지를 q에서 빼내 stack 에 쌓기.
        else:
            stack.append(q[top].pop(0))
            
    answer.reverse()
    
    return answer
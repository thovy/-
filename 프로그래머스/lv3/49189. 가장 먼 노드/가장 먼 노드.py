def solution(n, edge):
    answer = 0
    
    # https://jsikim1.tistory.com/318
    
    # 인접 노드 정보를 담아둘 adj
    adj = [[] for _ in range(n + 1)]
    for v1, v2 in edge:
        adj[v1].append(v2)
        adj[v2].append(v1)

    # print(adj)
    # [[], [3, 2], [3, 1, 4, 5], [6, 4, 2, 1], [3, 2], [2], [3]]
    
    # 방문한 노드라는 걸 check
    check = [0]*(n + 1)
    # 1번 노드에서 시작하므로 1번 방문 1
    check[1] = 1
    
    # print(check)
    # [0, 1, 0, 0, 0, 0, 0]
    
    q = [1]
    
    while q:
        current = q.pop(0)
        for i in adj[current]:
            if not check[i]:
                check[i] = check[current] + 1
                q.append(i)
                # print(check)
    
    answer = check.count(max(check))

    return answer
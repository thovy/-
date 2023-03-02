from collections import deque
def solution(n, computers):
    answer = 0
    
    isvisit = [0] * n
    
    def dfs(idx):
        isvisit[idx] = 1
        for side in range(n):
            if isvisit[side] == 0 and computers[idx][side]:
                dfs(side)
            print(isvisit)
    
    def bfs(idx):
        q = deque()
        q.append(idx)
        while q:
            i = q.popleft()
            isvisit[i] = 1
            for a in range(n):
                if computers[i][a] and isvisit[a] == 0:
                    q.append(a)
    
    for nodeidx in range(n):
        if isvisit[nodeidx] == 0:
            # dfs(nodeidx)
            bfs(nodeidx)
            answer += 1
    
    print(answer)
    return answer
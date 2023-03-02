def solution(n, computers):
    answer = 0
    
    isvisit = [0] * n
    
    def dfs(idx):
        isvisit[idx] = 1
        for side in range(n):
            if isvisit[side] == 0 and computers[idx][side]:
                dfs(side)
    
    for nodeidx in range(n):
        if isvisit[nodeidx] == 0:
            dfs(nodeidx)
            answer += 1
    
    return answer
def solution(board):
    answer = 0
    
    boundery = [[1,0],[1,1],[0,1],[-1,1],[-1,0],[-1,-1],[0,-1],[1,-1]]
    
    bsize = len(board)
    
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 1:
                for b in boundery:
                    if i+b[0] < bsize and i+b[0] >= 0 and j+b[1] < bsize and j+b[1] >= 0 and board[i+b[0]][j+b[1]] == 0:
                        board[i+b[0]][j+b[1]] = 2
    
    for ground in board:
        safezone = ground.count(0)
        answer += safezone
    
    return answer
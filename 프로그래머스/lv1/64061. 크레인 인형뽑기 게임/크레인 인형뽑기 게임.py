def solution(board, moves):
    answer = 0
    
    new_board = list(map(list, zip(*board)))
    stack = []
    
    for m in moves:
        for idx in range(len(new_board[m-1])):
            if new_board[m-1][idx] != 0:
                stack.append(new_board[m-1][idx])
                new_board[m-1][idx] = 0
                break
                
        if len(stack)>=2 and stack[-1] == stack[-2]:
            answer += 2
            stack.pop()
            stack.pop()
            # stack.remove(stack[-1])
            # stack.remove(stack[-1])
    return answer
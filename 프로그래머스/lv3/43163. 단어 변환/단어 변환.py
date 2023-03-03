from collections import deque
def solution(begin, target, words):
    answer = 1
    
    if target not in words:
        return 0
    
    # target 과 words 의 요소 하나를 비교,
    # 틀린 갯수가 하나면 그 단어 deque 에 넣기
    # 넣고 answer += 1
    # 그 단어를 popleft 하면서 다시 words 의 요소와 비교
    
    q = deque()
    q.append([begin, 0])
    isvisited = [0] * len(words)
    
    while q:
        word, cnt = q.popleft()
        if word == target:
            answer = cnt
            return answer
        else:
            for i in range(len(words)): # words 리스트의 길이(갯수)
                wrong = 0
                if isvisited[i] == 0:
                    for j in range(len(word)):  # word의 글자 갯수
                        if words[i][j] != word[j]:
                            wrong += 1
                    if wrong == 1:
                        q.append([words[i], cnt+1])
                        isvisited[i] = 1
                        
    return answer
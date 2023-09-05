import re
def solution(quiz):
    answer = []
    for q in quiz:
        words = list(map(str, q.split(' ')))
        total = 0
        sign = 1
        for w in words[:-1]:
            if w != '-' and w != '+' and w != "=":
                total += sign * int(w)
                sign = 1
            else:
                if w == '-':
                    sign = -1
                elif w == '+':
                    sign = 1
        if total == int(words[-1]):
            answer.append('O')
        else:
            answer.append('X')
    return answer
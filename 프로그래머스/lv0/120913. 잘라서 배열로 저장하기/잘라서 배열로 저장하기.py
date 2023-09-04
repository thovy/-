def solution(my_str, n):
    answer = []
    def slicing(word):
        answer.append(word[:n])

        if len(word[n:]) > n:
            slicing(word[n:])
        elif word[n:] != "":
            answer.append(word[n:])
    
    slicing(my_str)

    return answer
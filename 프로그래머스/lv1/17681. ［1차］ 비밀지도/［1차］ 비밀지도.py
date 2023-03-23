def solution(n, arr1, arr2):
    answer = [""]*n
    
    # zfill(n) : 글자수 n이 되도록 0 채우기
    a1 = list(format(i, 'b').zfill(n) for i in arr1)
    a2 = list(format(i, 'b').zfill(n) for i in arr2)
    
    for i in range(len(a1)):
        for j in range(len(a1[i])):
            # 0 이면 안 됨. "0" 이어야 됨
            if a1[i][j] == "0" and a2[i][j] == "0":
                answer[i] += " "
            else:
                answer[i] += "#"
    
    return answer
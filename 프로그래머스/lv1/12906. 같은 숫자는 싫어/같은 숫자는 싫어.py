def solution(arr):
    answer = []
    
    
    n = arr[0]
    answer.append(n)
    for i in range(1,len(arr)):
        if arr[i] == n:
            continue
        else:
            answer.append(arr[i])
            n = arr[i]
    
    
    return answer
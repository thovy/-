def solution(num, total):
    answer = []
    
    for i in range(0,101):
        if sum(range(i, i+num)) == total:
            return list(map(int, range(i,i+num)))
    
    for i in range(-100,0):
        if sum(range(i, i+num)) == total:
            return list(map(int, range(i,i+num)))
        
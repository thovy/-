def solution(number, limit, power):
    answer = 0
    
    for n in range(1,number+1):
        yaksu = 0
        # 그냥 약수 구하기 - 시간초과됨
        # for i in range(1, n+1):
        #     if n % i == 0:
        #         yaksu += 1
        
        # 신기한 약수 구하기
        for i in range(1, int(n**(1/2)) + 1):
            if n % i == 0:
                yaksu += 1
                if (i**2) != n:
                    yaksu += 1
        
        if yaksu <= limit:
            answer += yaksu
        else:
            answer += power
    # print(yaksu_gatsu)
    
    return answer
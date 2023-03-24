def solution(dartResult):
    answer = 0
    # dartResult 에 정수 10이 가능해 한자리씩 뽑아 구문하면 안 됨.
    # X 로 바꿔서 판단해주자. (예제 2)
    dartResult = dartResult.replace('10', 'X')
    # 제곱을 쉽게 계산하기 위해 dict 만들어줘서 해당하는 보너스가 나오면 바로 넣을 수 있게
    bonus = {"S":1, "D": 2, "T":3}
    chart = []
    
    for i in dartResult:
        # 숫자 판별함수 isdigit, X(10) 일 때,
        # 숫자를 먼저 chart 에 넣어줌
        if i.isdigit() or i == "X":
            if i == "X":
                chart.append(10)
            else:
                # i 는 str 이기 때문에 int로 바꿔주기
                chart.append(int(i))
        # 보너스일 땐, 앞에 있던 숫자를 빼와서 제곱해줌(뒤에서 빼기 때문에 pop)
        elif i in bonus:
            tmp = chart.pop()
            chart.append(tmp ** bonus[i])
        # 스타상(*)일 땐 마지막껄 2배해주는데, 해당점수와 직전 점수가 2배임.
        # 첫번째 점수에서 스타상이 나오면 해당점수만 2배
        # if chart 로 pop 한 뒤에도 chart 가 있는지 확인
        elif i == "*":
            tmp = chart.pop()
            if chart:
                # 맨 마지막[-1] 을 2배
                chart[-1] *= 2
            # chart 확인 후에 더해야겠지
            chart.append(tmp*2)
        # 아차상(#)은 해당 점수만 마이너스 이므로
        elif i == "#":
            tmp = chart.pop()
            chart.append(-1*tmp)
    answer = sum(chart)
    
    return answer
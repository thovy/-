def solution(users, emoticons):
    answer = [-1, -1]
    dc = [10, 20, 30, 40]
    n, m = len(users), len(emoticons)
    # 이모티콘들의 할인률 리스트
    dclist = [0]*m
    
    def dfs(idx):
        nonlocal answer
        # 마지막엔
        if idx == m:
            # 플러스가입자 plus_num, 이모티콘판매액 cost_num
            plus_num, cost_num = 0,0
            # 유저를 돌아가면서
            for i in range(n):
                tmp = 0
                # 이모티콘을 다 돌리면서
                for j in range(m):
                    # 현재 선택된 이모티콘 할인률이 user가 원하는 할인률보다 높으면 구매
                    # tmp = 이모티콘가격 * 할인률
                    # 그렇게 모든 이모티콘을 탐색하면 tmp 는 user 가 구매하게 될 가격이 되고,
                    if users[i][0] <= dclist[j]:
                        tmp += emoticons[j] * (100-dclist[j]) // 100
                # tmp 가 user 의 구매상한보다 크면
                # 이모티콘플러스 구매(plus_num +=1)
                # 아니면 이모티콘구매한 거 그대로 cost에 추가
                if tmp >= users[i][1]:
                    plus_num += 1
                else:
                    cost_num += tmp
            # 계산된 이플 가입자가 현재 이플 가입자보다 클 때,
            # 이플 가입자는 그대로인데, 이모티콘 판매액이 큰 경우엔 answer 에 넣기
            # 이플가입최대가 목표이므로 이플가입자가 작고 이판액이 큰 건 재낌
            if plus_num > answer[0] or plus_num == answer[0] and cost_num > answer[1]:
                answer = [plus_num, cost_num]
            return
        # 4번 돌면서 이모티콘 하나의 할인률이 1,2,3,4 일 때를 모두 만들어 넣기
        for i in range(4):
            dclist[idx] = dc[i]
            dfs(idx+1)
    
    dfs(0)
    
    return answer
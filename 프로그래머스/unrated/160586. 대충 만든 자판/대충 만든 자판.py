def solution(keymap, targets):
    answer = []
    
    while targets:
        click = 0
        target = targets.pop(0)
        # index 함수 - 찾는 원소가 처음 나오는 index 를 반환
        for t in target:
            tmp = 101
            for key in keymap:
                if t in key:
                    tmp = min(key.index(t)+1, tmp)
            if tmp == 101:
                # break 를 여기 해도 이번 for문 밖에서 answer.append(click) 을 하기 때문에
                # 여기선 answer.append(-1); break; 해선 안 됨.
                click = -1
                break
            click+= tmp
        answer.append(click)
    
    return answer
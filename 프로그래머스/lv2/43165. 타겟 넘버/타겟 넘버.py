from collections import deque
def solution(numbers, target):
    answer = 0
    
    # BFS
    
    # index 를 같이 넣어주기 위해 queue 사용하기
    queue = deque()
    # numbers 의 길이 n 만큼 돌아가며 모두 계산 해보기 위해
    n = len(numbers)
    # 시작을 1 과 -1 두개로 시작하기 위해, 첫번째 수 numbers[0] 와 그 index 인 0을 넣어줌
    queue.append([numbers[0],0])
    queue.append([-1*numbers[0],0])
    
    # 뒤에 하나씩 꺼내서 [0] 에다가 각각 +[1], -[1] 을 넣어 계산해 저장
    # 하나의 값에 +, - 두가지 경우를 더하게 됨
    # 그러면 쭊쭊 갈래를 치며 모든 경우를 탐색하게 된다.
    
    # queue 가 있을 때. 모두 꺼내서 계산 한 뒤에는 answer 을 뽑아야지
    while queue:
        # popleft 를 이용해 첫번째 들어갔던 경우를 temp, index 에 꺼내고,
        # 거기에다가 다음 수들을 더해줘 저장함
        temp, index = queue.popleft()
        index += 1
        if index < n:
            # +, - 모두 덱에 저장.
            queue.append([temp + numbers[index], index])
            queue.append([temp - numbers[index], index])
        else:
            # index 가 n 과 같아져 탐색할 경우의 수가 모두 queue 에 저장되었다면
            # 꺼내서 확인만 하면 됨.
            # 그래서 위에서 꺼낸 temp 가 target 과 같은 경우가 있다면 anwer 에 카운트 증가
            if temp == target:
                answer += 1
    return answer


#     # 재귀함수를 이용한 DFS
    
#     n = len(numbers)
    
#     # 재귀 돌릴 함수 선언
#     def dfs(index, result):
#         if index == n:
#             if result == target:
#                 # 전역변수는 아닌 함수 내 변수를 호출하는 nonlocal
#                 nonlocal answer
#                 answer += 1
#             # index 가 n 이면 끝내기
#             # 깊이가 n 에 닿으면 해당 깊이로 탐색은 끝난 거지.
#             # 그럼 그 때 numbers 를 모두 합한 result 가 target 과 같으면 answer += 1
#             return
#         else:
#             dfs(index+1, result + numbers[index])
#             dfs(index+1, result - numbers[index])
    
#     # 함수 시작
#     dfs(0,0)
#     return answer

# bfs 성능
# 테스트 1 〉	통과 (1148.34ms, 116MB)
# 테스트 2 〉	통과 (1013.49ms, 116MB)
# 테스트 3 〉	통과 (0.67ms, 10.4MB)
# 테스트 4 〉	통과 (1.87ms, 10.5MB)
# 테스트 5 〉	통과 (16.81ms, 13.2MB)
# 테스트 6 〉	통과 (0.96ms, 10.4MB)
# 테스트 7 〉	통과 (0.46ms, 10.4MB)
# 테스트 8 〉	통과 (5.50ms, 10.7MB)

# 재귀함수 dfs 성능
# 테스트 1 〉	통과 (307.65ms, 10.2MB)
# 테스트 2 〉	통과 (298.41ms, 10.2MB)
# 테스트 3 〉	통과 (0.30ms, 10.3MB)
# 테스트 4 〉	통과 (2.50ms, 10.2MB)
# 테스트 5 〉	통과 (9.06ms, 10.2MB)
# 테스트 6 〉	통과 (0.59ms, 10.2MB)
# 테스트 7 〉	통과 (0.55ms, 10.4MB)
# 테스트 8 〉	통과 (2.71ms, 10.1MB)
            
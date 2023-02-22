from collections import deque
import sys
N, L = map(int, sys.stdin.readline().split())
A = list(map(int, sys.stdin.readline().split()))

answerdeque = deque()

for i in range(N):
    # answerdeque 의 맨 뒤의 값([-1][0])이  A[i] 의 값보다 크면
    while answerdeque and answerdeque[-1][0] > A[i]:
        answerdeque.pop()    # 맨 마지막 값 뒤로 빼내기.
        # pop()- 마지막 값 뒤로 빼내기, popleft()- 첫 값 앞으로 빼내기
        # append()- 마지막 값으로 넣기, appendleft()- 첫 값으로 넣기
    # 마지막값 빼낸 뒤 현재 값 A[i] 넣기
    answerdeque.append((A[i], i))    # deque 에 인덱스 값 넣기
    if answerdeque[0][1] <= i - L:    # 범위를 벗어나면
        answerdeque.popleft()        # 첫번째 값 제거
    print(answerdeque[0][0], end=" ")
        
    
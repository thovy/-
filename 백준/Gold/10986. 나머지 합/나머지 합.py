import sys
# N 수열의 개수
# M 나눌 수
N, M = map(int, sys.stdin.readline().split())
A = list(map(int,sys.stdin.readline().split()))

# 수열의 개수 N 으로 구간 합 배열 초기화
S = [0] * N
# 합 배열을 M 으로 나눈 나머지 배열 초기화
# ( 나눈 나머지를 저장할 거라 M=3 이면 1, 2, 3 만 있으면 됨. 그들의 갯수를 저장할 거니까)
C = [0] * M

answer = 0

# 구간 합 배열 S 넣기
S[0] = A[0]    # 첫번째
for i in range(1, N):
    S[i] = S[i-1] + A[i]

# 나머지 C 구하기
for i in range(N):
    remainder = S[i] % M
    if remainder == 0:
        answer += 1
    C[remainder] += 1    # 나머지로 나온 remainder 의 갯수 세기

for i in range(M):
    if C[i] > 1: # 나머지로 나온 수가 2이상이면 더하기
        answer += (C[i] * (C[i] - 1) // 2)    # 경우의 수 nCn-1 을 계산해서 answer 에 더하기

print (answer)
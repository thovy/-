import sys
import copy

N, M = map(int, sys.stdin.readline().split())

A = [[0] * M for _ in range(N)]
B = copy.deepcopy(A)
answer = copy.deepcopy(A)

for ay in range(N):
    tmp_list = list(map(int, sys.stdin.readline().split()))
    for ax in range(M):
        A[ay][ax] = tmp_list[ax]
        
for by in range(N):
    tmp_list = list(map(int, sys.stdin.readline().split()))
    for bx in range(M):
        B[by][bx] = tmp_list[bx]

for y in range(N):
    for x in range(M):
        answer[y][x] = A[y][x] + B[y][x]

for i in range(N):
    print(' '.join(map(str, answer[i])))

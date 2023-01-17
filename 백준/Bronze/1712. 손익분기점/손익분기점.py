import sys;
A, B, C = map(int, sys.stdin.readline().split())

answer = -1

if B >= C:
    print(answer)
elif B < C:
    answer = int(A/(C-B))+1
    print(answer)
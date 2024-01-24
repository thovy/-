import sys

N, K = map(int, sys.stdin.readline().split())

yaksu_list = []

for n in range(1, N+1):
    if N % n == 0:
        yaksu_list.append(n)

    if len(yaksu_list) == K:
        print(yaksu_list[K-1])
        break

if len(yaksu_list) < K:
    print(0)
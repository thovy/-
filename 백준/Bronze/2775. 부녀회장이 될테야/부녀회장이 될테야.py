import sys
T = int(sys.stdin.readline())

for _ in range(T):
    k = int(sys.stdin.readline())
    n = int(sys.stdin.readline())
    # 0 층의 n 호 까지 리스트
    floor0 = [x for x in range(1, n + 1)]
    for i in range(k):
        for i in range(1, n):
            floor0[i] += floor0[i-1]
    print(floor0[-1])
import sys
T = int(sys.stdin.readline())

# 거스름돈 단위
Q, D, N, P = 25, 10, 5, 1

for _ in range(T):
    charge = int(sys.stdin.readline())

    # 거스름돈 갯수 - 거슬러줄 동전의 갯수
    # 매 거스름돈 마다 새롭게 시작해야함.
    cq, cd, cn, cp = 0, 0, 0, 0

    while charge > 0:
        if charge >= Q:
            cq = charge // Q
            charge = charge % Q
        elif charge >= D:
            cd = charge // D
            charge = charge % D
        elif charge >= N:
            cn = charge // N
            charge = charge % N
        else:
            cp = charge // P
            charge = charge % P

    print(cq, cd, cn, cp)
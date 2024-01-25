import sys

while True:
    N = int(sys.stdin.readline())
    if N == -1:
        break

    yaksu_list = []

    for n in range(1, N+1):
        if N % n == 0:
            yaksu_list.append(n)

    if (sum(yaksu_list)-N) == N:
        answer = str(N) + " = "
        print(answer + (" + ".join(map(str, yaksu_list[:-1]))))
    else:
        print(str(N) + " is NOT perfect.")
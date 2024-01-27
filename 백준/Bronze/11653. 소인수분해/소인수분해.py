import sys

N = int(sys.stdin.readline())

yaksu_list = []
while True:
    if N == 1:
        break

    sosu = True
    for n in range(2, N+1):
        if N % n == 0:
            sosu = False
            N = N // n
            yaksu_list.append(n)
            break

    if sosu == True:
        break

print('\n'.join(map(str, yaksu_list)))
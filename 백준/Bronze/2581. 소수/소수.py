import sys

M = int(sys.stdin.readline())
N = int(sys.stdin.readline())

sosu_list = []
for num in range(M, N+1):
    if num == 1:
        continue
        
    yaksu_list = []
    for n in range(2, num):
        if num % n == 0:
            yaksu_list.append(n)
            break
    if len(yaksu_list) == 0:
        sosu_list.append(num)

if len(sosu_list) == 0:
    print(-1)
else:
    print(sum(sosu_list))
    print(sosu_list[0])
import sys

# 주어지는 수의 갯수
N = int(sys.stdin.readline())
# 주어지는 수 list
num_list = list(map(int, sys.stdin.readline().split()))

# list에서 소수의 갯수
answer = 0

for num in num_list:
    yaksu_list = []
    if num == 1:
        continue

    for n in range(2, num):
        # num을 나눌 수 있는 수가 있다면 break
        if num % n == 0:
            yaksu_list.append(n)
            break

    if len(yaksu_list) == 0:
        answer += 1

print(answer)
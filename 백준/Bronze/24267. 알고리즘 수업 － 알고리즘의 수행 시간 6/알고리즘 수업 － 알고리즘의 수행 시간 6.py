import sys

n = int(sys.stdin.readline())
answer = 0
# 시간초과
# for i in range(n-1):
#     for j in range(i):
#         answer += j

# 2번째
for i in range(n-1):
    answer += ((i)*(i+1)) // 2

print(answer)

print(3)

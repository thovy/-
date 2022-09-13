import sys
input = sys.stdin.readline

N, M = map(int, input().split())
numbers = list(map(int, input().split()))
prefix_sum = [0]

tmp = 0
for i in numbers:
    tmp = tmp + i
    prefix_sum.append(tmp)

for i in range(M):
    startNum, endNum = map(int, input().split())
    answer = prefix_sum[endNum] - prefix_sum[startNum-1]
    print(answer)
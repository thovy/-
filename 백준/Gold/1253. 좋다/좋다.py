import sys
input = sys.stdin.readline
n = int(input())    # 수의 개수
A = list(map(int, input().split()))    # 수 리스트
count = 0    # 좋은 수 개수

# 차례로 정렬 해서 더해가보자
A.sort()

# k 를 넣고 k 가 움직임에 따라 j 를 움직이므로써 한 번에 계산할 수 있을 듯
# 좋은 수를 만들 수 있는 경우의 수를 찾는 게 아니라
# 리스트에서 좋은 수의 갯수를 찾는 것이므로 k 가 한 번만 지나가면 됨.
for k in range(n):
    findanswer = A[k]
    i = 0
    j = n-1    # 왜 k -1 이 아니지? 아 k가 0일수가 있구나
    while i < j:    # index error 가 날 수도 있음.
        if A[i] + A[j] == findanswer:
            if i != k and j != k:
                count += 1
                break    # 브레이크 안 해주면 안 됨
            elif i == k:
                i += 1
            elif j == k:
                j -= 1
        elif A[i] + A[j] < findanswer:
            i += 1
        else:
            j -= 1
print(count)    
import sys
input = sys.stdin.readline
n = int(input())    # 재료 종류 수
m = int(input())    # 갑옷만드는데필요한 재료 수
ns = list(map(int, input().split()))    # 재료들 리스트
# 그래서 ns 리스트의 값들의 합이 m 이 되면 갑옷 하나 완성

# ns 를 정렬을 안 하면, start 를 움직일지 end를 움직일지 정하기 힘듬.
ns.sort()

i = 0    # start index
j = len(ns)-1    # end index
# i는 처음부터 증가하면서 다음칸으로 이동하고
# j는 마지막부터 감소하면서 다음칸으로 이동해야 중복이 없음.
# i j  모두 1 에서 시작하면 다음칸으로 이동할 때 썼던 재료를 또 쓰는 중복이 생김.
count = 0

while i < j:
    sum = ns[i] + ns[j]
    if sum == m:
        count += 1
        j -= 1
        # 재료는 한 번 사용하는 거기 때문에 모두 옮겨줘야함.
        i += 1
    elif sum > m:
        j -= 1
    else:
        i += 1
        
print(count)
        
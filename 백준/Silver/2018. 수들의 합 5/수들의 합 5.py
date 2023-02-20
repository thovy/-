import sys
n = int(sys.stdin.readline())

# end index 가 마지막 수에 닿았을 때는 start index 와 end index 가 모두 마지막 수에 닿아있을 때만
# sum 이 마지막 수가 되므로 count 1 해놓고 end index 만 마지막 수에 닿으면 탐색 끝내기
# 그래서 마지막 count 1 해놓기
count = 1

sindex = 1
eindex = 1

# s e 모두 1 이므로 sum 도 1
sum = 1

# e 가 n 보다 작을 때지
while eindex != n:
    if sum == n:    # start 와 end 까지의 합이 n 과 같다면
        count += 1    # 경우의 수 count + 1
        eindex += 1    # 경우의 수를 셌으니 다음으로 e 이동
        sum += eindex    # e 를 이동했으니 sum 다시 더하기
    elif sum >= n:    # sum 이 n 보다 크면 start 움직이기
        sum -= sindex    # 먼저 저장된 값만큼 빼주고 start 이동시켜야함
        sindex += 1
    else:            # sum 이 n 보다 작으면 end 이동
        eindex += 1
        sum += eindex
print (count)
import sys;
n = int(sys.stdin.readline())

for i in range(n):
    case = list(map(int, sys.stdin.readline().split()))
    a = case[0]
    total = sum(case) - a
    avg = total/a
    count = 0
    for j in case[1:]:
        if j > avg:
            count += 1
    # print(str(round((count/a)*100, 3)) + '%')
    print(f'{count/a * 100:.3f}%')
    
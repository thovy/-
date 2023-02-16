import sys
a = int(sys.stdin.readline())

for _ in range(a):
    H, W, N = map(int, sys.stdin.readline().split())
    number = int(N/H) + 1
    floor =  int(N%H)
    
    if floor == 0:
        floor = H
        number -= 1
    
    if number < 10:
        answer = str(floor) + "0" + str(number)
    else:
        answer = str(floor) + str(number)
    print(answer)
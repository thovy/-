import sys;
N = int(sys.stdin.readline())

def hansufunc(N):
    count = 0
    for i in range(1,N+1):
        nList = list(map(int,str(i)))
        if i <100:
            count += 1
        elif nList[1] - nList[0] == nList[2] - nList[1]:
            count += 1
    return count

print(hansufunc(N))
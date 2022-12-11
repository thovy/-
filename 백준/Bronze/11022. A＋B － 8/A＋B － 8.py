import sys;
a = int(sys.stdin.readline())

for i in range(a):
    x, y = map(int, sys.stdin.readline().split())
    print("Case #{}: {} + {} = {}".format(i+1, x, y, x+y))
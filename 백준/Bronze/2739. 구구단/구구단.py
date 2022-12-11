import sys;
a = int(sys.stdin.readline())

for i in range(1,10):
    print("{} * {} = {}".format(a, i, a*i))
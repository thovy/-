import sys;
x, y = map(int, sys.stdin.readline().split());

if y < 45:
    if x != 0:
        print("{} {}".format(x-1,y+15))
    else:
        print("23 {}".format(y+15))
else:
    print("{} {}".format(x, y-45))
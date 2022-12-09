import sys;
x, y = map(int, sys.stdin.readline().split());
z = int(sys.stdin.readline());

minute = y+z
hour = int(minute/60)

if minute >= 60:
    if x + hour >23:
        print("{} {}".format(x+hour-24, minute%60))
    else:
        print("{} {}".format(x+hour, minute%60))
else:
    print("{} {}".format(x, minute))
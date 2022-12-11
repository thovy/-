import sys;
z=True
while(z):
    x, y = map(int, sys.stdin.readline().split())
    if x == 0 and y ==0:
        z=False
    else:
        print(x+y)
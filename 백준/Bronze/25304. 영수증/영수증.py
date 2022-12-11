import sys;
totalsum = int(sys.stdin.readline())
kind = int(sys.stdin.readline())
total = 0

for i in range(kind):
    x, y = map(int, sys.stdin.readline().split())
    total += (x*y)
    
if total == totalsum:
    print("Yes")
else:
    print("No")
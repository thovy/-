import sys
x = int(sys.stdin.readline())
numlist = list(map(int, sys.stdin.readline().split()))
    
print("{} {}".format(min(numlist), max(numlist)))
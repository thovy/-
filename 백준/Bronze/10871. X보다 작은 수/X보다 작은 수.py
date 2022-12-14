import sys
x, y = map(int, sys.stdin.readline().split())
numlist = list(map(int, sys.stdin.readline().split()))

for i in numlist:
    if i < y:
        print(i)
import sys
a = sys.stdin.readline()
numlist = list(map(int, sys.stdin.readline().split()))
foundnum = int(sys.stdin.readline())

answer = numlist.count(foundnum)

print(answer)
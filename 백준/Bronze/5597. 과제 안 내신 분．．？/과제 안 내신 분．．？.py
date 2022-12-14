import sys
numlist = []

for i in range(28):
    numlist.append(int(sys.stdin.readline()))

for j in range(1,31):
    if j not in numlist:
        print(j)
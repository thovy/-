import sys;
numlist = list(map(int, sys.stdin.readline().split()));
countlist=[]

for i in numlist:
    countlist.append(numlist.count(i))

if 3 in countlist:
    print(10000 + (numlist[0]*1000))
elif 2 in countlist:
    index = countlist.index(2)
    print(1000 + (numlist[index])*100)
else:
    maxnum = max(numlist)
    print(maxnum*100)
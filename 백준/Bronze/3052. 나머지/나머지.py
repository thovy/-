import sys;
setlist = set([])

for i in range(10):
    a = int(sys.stdin.readline())
    setlist.add(int(a%42))

print(len(setlist))
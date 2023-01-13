import sys;
s = str(sys.stdin.readline())


for j in range(ord('a'),ord('z')+1):
    print(s.find(chr(j)))
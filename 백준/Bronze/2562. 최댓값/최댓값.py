import sys;
a, maxnum, answerindex = 0, 0, 0

for i in range(9):
    a = int(sys.stdin.readline())
    if a > maxnum:
        maxnum = a
        answerindex = i+1

print(maxnum)
print(answerindex)
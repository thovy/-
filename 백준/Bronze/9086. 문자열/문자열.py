import sys;
n = int(sys.stdin.readline());

for _ in range(n):
    s = str(input());
    answer = s[0] + s[-1];
    print(answer);
import sys;
N = int(sys.stdin.readline())

dohwaji = [[0] * 100 for _ in range(100)]

for _ in range(N):
    y, x = map(int, sys.stdin.readline().split())
    for yi in range(y, y + 10):
        for xi in range(x, x + 10):
            dohwaji[yi][xi] = 1

answer = 0
for line in dohwaji:
    answer += sum(line)

print(answer)
import sys

N = int(sys.stdin.readline())

dot = 2
line = dot - 1
# square는 굳이? 필요없는 거 같음 ; 왜 계산했지?
# square = line * line
total_dot = dot * dot

for _ in range(N):
    dot = dot + line
    line = dot - 1
    # square = line * line
    total_dot = dot * dot

print(total_dot)
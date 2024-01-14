N = int(input());

for b in range(1, 2*N):
    if b > N:
        blankN = b - N
        starN = (2 * N)-b
    else:
        blankN = N - b
        starN = b
    blank = " " * blankN
    star = "*" * starN
    backStar = "*" * (starN - 1)
    answer = blank + star + backStar;
    print(answer);
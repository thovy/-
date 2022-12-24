import sys;
n = int(sys.stdin.readline())

for i in range(n):
    score = 0
    case = str(sys.stdin.readline())
    count = 0
    for j in case:
        if j == "O":
            count +=1
            score += count
        else:
            count = 0
            
    print(score)
        
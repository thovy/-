word = str(input())

def checkNum(alphabet):
    if (alphabet == 'A') or (alphabet == 'B') or (alphabet == 'C'):
        return 2
    elif (alphabet == 'D') or (alphabet == 'E') or (alphabet == 'F'):
        return 3
    elif (alphabet == 'G') or (alphabet == 'H') or (alphabet == 'I'):
        return 4
    elif (alphabet == 'J') or (alphabet == 'K') or (alphabet == 'L'):
        return 5
    elif (alphabet == 'M') or (alphabet == 'N') or (alphabet == 'O'):
        return 6
    elif (alphabet == 'P') or (alphabet == 'Q') or (alphabet == 'R') or (alphabet == 'S'):
        return 7
    elif (alphabet == 'T') or (alphabet == 'U') or (alphabet == 'V'):
        return 8
    elif (alphabet == 'W') or (alphabet == 'X') or (alphabet == 'Y') or (alphabet == 'Z'):
        return 9

time = 0
for i in range(len(word)):
    time += checkNum(word[i]) +1

print(time)
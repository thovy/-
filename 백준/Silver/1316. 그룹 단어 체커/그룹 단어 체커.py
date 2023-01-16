import sys;
N = int(sys.stdin.readline())

answer = N
for _ in range(N):
    word = str(input())
    for i in range(len(word)-1):
        if word[i+1] == word[i]:
            continue
        elif word[i] in word[i+1:]:
            answer -= 1
            break
print(answer)
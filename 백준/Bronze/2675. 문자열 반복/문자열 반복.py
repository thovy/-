s = int(input())

for i in range(s):
    num, word = input().split()
    for w in word:
        print(w*int(num), end='')
    print()
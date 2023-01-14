import sys;
word = input()

word = word.upper()
maxcnt = 0
maxword = ''
for i in set(word):
    num = word.count(i)
    if num > maxcnt:
        maxcnt = num
        maxword = i
    elif num == maxcnt:
        maxcnt = num
        maxword = '?'
    else:
        continue

print(maxword)
    
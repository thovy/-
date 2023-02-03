x = int(input())

# 몇번째 열
line = 0
# 몇번째 행
row = 0
while x > row:
    line += 1
    row += line

gap = row - x
if line % 2 == 0:
    top = line - gap
    under = gap + 1
else:
    top = gap + 1
    under = line - gap
print(f'{top}/{under}')
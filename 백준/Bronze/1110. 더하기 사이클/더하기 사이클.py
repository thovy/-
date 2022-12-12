import sys
a = sys.stdin.readline()
count = 0
answer = 0
x, y, z = 0,0,0

if int(a) == 0:
  count += 1
  answer = a
elif int(a) < 10:
    x = 0
    y = int(a)
else:
    x = int(a[0])
    y = int(a[1])

while (int(a) != int(answer)):
    z= str(int(x)+int(y))
    if int(z) < 10:
        answer = str(y)+str(z)
    else:
        answer = str(y)+str((z)[1])
    
    if a != answer:
        x = y
        y = answer[1]

    count += 1
    
print(count)
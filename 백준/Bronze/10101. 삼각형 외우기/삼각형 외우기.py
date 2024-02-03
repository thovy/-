import sys

a1 = int(sys.stdin.readline())
a2 = int(sys.stdin.readline())
a3 = int(sys.stdin.readline())
total_angle = a1 + a2 + a3

if a1 == 60 and a2 == 60 and a3 == 60:
    print("Equilateral")
elif total_angle == 180:
    if a1 == a2 or a1 == a3 or a2 == a3:
        print("Isosceles")
    else:
        print("Scalene")
else:
    print("Error")
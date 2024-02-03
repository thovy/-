import sys

while True:
    a1, a2, a3 = map(int, sys.stdin.readline().split())
    if a1 == 0:
        break
    angle_list = [a1, a2, a3]
    sorted_a_list = sorted(angle_list)
    if sorted_a_list[2] >= (sorted_a_list[0]+sorted_a_list[1]):
        print("Invalid")
        continue
        
    if a1 == a2 and a1 == a3:
        print("Equilateral")
    elif a1 == a2 or a1 == a3 or a2 == a3:
        print("Isosceles")
    else:
        print("Scalene")
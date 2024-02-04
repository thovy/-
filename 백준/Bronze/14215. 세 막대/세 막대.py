import sys

line_list = list(map(int, sys.stdin.readline().split()))

sorted_list = sorted(line_list)

if sum(sorted_list[:2]) > sorted_list[2]:
    print(sum(sorted_list))
else:
    print((sum(sorted_list[:2]) * 2) -1)
import sys
x, y, w, h = map(int, sys.stdin.readline().split())

width_gap = w-x
height_gap = h-y

print(min(width_gap, x, height_gap, y))
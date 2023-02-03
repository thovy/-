import sys
import math
a, b, v = map(int, sys.stdin.readline().split())
# 나무높이 v
# 낮 a 밤 b

# 달팽이 현재 위치 hight
day = (v - b)/(a-b)

print(math.ceil(day))
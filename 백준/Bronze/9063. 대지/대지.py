import sys

N = int(sys.stdin.readline())

x_list = []
y_list = []

for _ in range(N):
    x, y = map(int, sys.stdin.readline().split())
    x_list.append(x)
    y_list.append(y)

area = 0
if len(x_list) <= 1:
    area = 0
else:
    max_x = max(x_list)
    min_x = min(x_list)
    max_y = max(y_list)
    min_y = min(y_list)
    
    x_line = max_x - min_x
    y_line = max_y - min_y
    
    area = x_line * y_line
    
print(area)
